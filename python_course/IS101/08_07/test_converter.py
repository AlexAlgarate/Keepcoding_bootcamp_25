import pytest

from src.converters.roman_converter import (
    RomanConverter,
    create_roman_calculator,
)
from src.converters.utils import roman_exceptions as exc
from src.converters.utils.roman_validator import RomanNumeralValidator


@pytest.fixture
def converter() -> RomanConverter:
    converter = create_roman_calculator()
    return converter


@pytest.fixture
def validator() -> RomanNumeralValidator:
    return RomanNumeralValidator()


class TestValidateRomanString:
    @pytest.mark.parametrize(
        "valid_roman",
        ["III", "III", "IV", "V", "IX", "X", "XXVII", "XLVIII", "LIX", "XCIII"],
    )
    def test_valid_roman_patterns(
        self, validator: RomanNumeralValidator, valid_roman: str
    ) -> None:
        assert validator.is_valid_roman(valid_roman)

    @pytest.mark.parametrize(
        "invalid_roman", ["IIII", "VV", "LL", "DD", "IC", "IM", "XM", "MMMM"]
    )
    def test_invalid_roman_patterns(
        self, validator: RomanNumeralValidator, invalid_roman
    ) -> None:
        assert validator.is_valid_roman(invalid_roman) is False

    @pytest.mark.parametrize(
        "valid_arabic_input, valid_arabic_expected",
        [
            (1, 1),
            (2, 2),
            (3, 3),
            (5000, 5000),
            (123456789, 123456789),
            (int(6.022e23), int(6.022e23)),
            (5.0, 5.0),
            (3999.0, 3999.0),
        ],
    )
    def test_valid_arabic_input(
        self,
        validator: RomanNumeralValidator,
        valid_arabic_input: int,
        valid_arabic_expected: int,
    ) -> None:
        assert (
            validator.validate_arabic_input(valid_arabic_input) == valid_arabic_expected
        )

    @pytest.mark.parametrize(
        "invalid_arabic_input",
        [
            "1",
            "1000.0",
            [1, 2, 3],
            {1: 1.5},
        ],
    )
    def test_invalid_arabic_inputs(
        self, validator: RomanNumeralValidator, invalid_arabic_input: int
    ) -> None:
        with pytest.raises(
            exc.NumberOutOfRangeError, match="El número debe ser numérico"
        ):
            validator.validate_arabic_input(invalid_arabic_input)

    @pytest.mark.parametrize(
        "valid_arabic_float,expected_number",
        [
            (1.0, 1),
            (10000.0, 10000),
            (123456789.0, 123456789),
        ],
    )
    def test_number_is_a_valid_float(
        self,
        validator: RomanNumeralValidator,
        valid_arabic_float: int,
        expected_number: int,
    ) -> None:
        assert validator.validate_arabic_input(valid_arabic_float) == expected_number

    @pytest.mark.parametrize(
        "invalid_arabic_float",
        [1.5, 10000.1, 1234.56789],
    )
    def test_number_is_not_valid_float(
        self, validator: RomanNumeralValidator, invalid_arabic_float: int
    ) -> None:
        with pytest.raises(
            exc.NumberOutOfRangeError, match="El número debe ser entero"
        ):
            validator.validate_arabic_input(invalid_arabic_float)

    def test_number_smaller_1(self, validator: RomanNumeralValidator) -> None:
        with pytest.raises(
            exc.NumberOutOfRangeError, match="El número debe ser mayor a 0. Recibido"
        ):
            validator.validate_arabic_input(0)

    @pytest.mark.parametrize(
        "input_str,expected_output",
        [
            ("XVI", "XVI"),
            ("xvi", "XVI"),
            ("  xvi  ", "XVI"),
            ("\tXVI\n", "XVI"),
            ("mcmxcix", "MCMXCIX"),
            (" MMMCMXCIX ", "MMMCMXCIX"),
        ],
    )
    def test_valid_strings(
        self, validator: RomanNumeralValidator, input_str: str, expected_output: str
    ) -> None:
        assert validator.validate_roman_input(input_str) == expected_output

    @pytest.mark.parametrize(
        "roman",
        [
            1,
            1.1,
            True,
            [1, 2, 3],
            {"roman_value": [1, 2, 3, 4.5]},
        ],
    )
    def test_invalid_type_for_roman(
        self, validator: RomanNumeralValidator, roman: str
    ) -> None:
        with pytest.raises(
            exc.InvalidRomanNumeralError, match="El valor debe ser una cadena de texto"
        ):
            validator.validate_roman_input(roman)

    @pytest.mark.parametrize(
        "invalid_input",
        [
            "",
            "   ",
            "\n\t",
        ],
    )
    def test_invalid_empty_string(
        self, validator: RomanNumeralValidator, invalid_input: str
    ) -> None:
        with pytest.raises(exc.InvalidRomanNumeralError, match="Cadena romana vacía."):
            validator.validate_roman_input(invalid_input)


class TestStandardRomanConverterToRoman:
    @pytest.mark.parametrize(
        "arabic,expected_roman",
        [
            (1, "I"),
            (4, "IV"),
            (9, "IX"),
            (58, "LVIII"),
            (3999, "MMMCMXCIX"),
            (1000, "M"),
            (1987, "MCMLXXXVII"),
            (2023, "MMXXIII"),
        ],
    )
    def test_valid_arabic_to_roman(
        self,
        converter: RomanConverter,
        arabic: int,
        expected_roman: str,
    ) -> None:
        assert converter._standard_converter.to_roman(arabic) == expected_roman

    @pytest.mark.parametrize(
        "arabic",
        [
            0,
            -1,
            -100,
            4000,
            5000,
            10000,
            999999,
        ],
    )
    def test_number_out_of_range(self, converter: RomanConverter, arabic: int) -> None:
        with pytest.raises(exc.NumberOutOfRangeError, match="Número fuera del rango"):
            converter._standard_converter.to_roman(arabic)

    def test_raise_exception_when_you_try_to_modify_dictionaries(
        self, converter: RomanConverter
    ):
        with pytest.raises(TypeError) as exc:
            converter._standard_converter._arabic_to_roman[123] = "123"  # type: ignore

            converter._standard_converter.to_roman(123)
            assert "'mappingproxy' object does not support item assignment" == exc.value

    @pytest.mark.parametrize(
        "arabic_input,expected_non_used_roman",
        [
            (1, "I"),
            (2, "II"),
            (30, "XXX"),
            (400, "CD"),
            (3999, "MMMCMXCIX"),
        ],
    )
    def test_from_roman_to_arabic_to_roman(
        self,
        converter: RomanConverter,
        arabic_input: int,
        expected_non_used_roman: str,
    ) -> None:
        roman = converter.to_roman(arabic_input)
        result = converter.to_arabic(roman)
        assert result == arabic_input

    @pytest.mark.parametrize(
        "non_used_arabic,input_roman",
        [
            (1, "I"),
            (2, "II"),
            (30, "XXX"),
            (400, "CD"),
            (3999, "MMMCMXCIX"),
        ],
    )
    def test_from_arabic_to_roman_to_arabic(
        self,
        converter: RomanConverter,
        non_used_arabic: int,
        input_roman: str,
    ) -> None:
        arabic = converter.to_arabic(input_roman)
        result = converter.to_roman(arabic)
        assert result == input_roman


class TestStandardRomanConverterToArabic:
    @pytest.mark.parametrize(
        "roman_input,expected_arabic",
        [
            ("I", 1),
            ("II", 2),
            ("III", 3),
            ("IV", 4),
            ("V", 5),
            ("IX", 9),
            ("X", 10),
            ("XXVII", 27),
            ("XLVIII", 48),
            ("LIX", 59),
            ("XCIII", 93),
            ("CXLI", 141),
            ("CLXIII", 163),
            ("CDII", 402),
            ("DLXXV", 575),
            ("CMXI", 911),
            ("MXXIV", 1024),
            ("MCCXXXIV", 1234),
            ("MDXLIX", 1549),
            ("MMM", 3000),
            ("MMMCMXCIX", 3999),
        ],
    )
    def test_valid_roman_to_arabic(
        self,
        converter: RomanConverter,
        roman_input: str,
        expected_arabic: int,
    ) -> None:
        assert converter._standard_converter.to_arabic(roman_input) == expected_arabic

    @pytest.mark.parametrize(
        "invalid_roman",
        [
            "A",
            "BXI",
            "123",
            "!@#",
            "MMMMM",
            "IL",
            "xm",
            "VX",
            "IVIV",
            "VV",
            "DM",
            "LC",
            "XLXL",
            "CMCM",
            "",
            "   ",
            "\n\t",
        ],
    )
    def test_invalid_roman_raises(
        self, converter: RomanConverter, invalid_roman: str
    ) -> None:
        with pytest.raises(exc.InvalidRomanNumeralError):
            converter._standard_converter.to_arabic(invalid_roman)

    @pytest.mark.parametrize(
        "insensitive_cases,expected_arabic",
        [
            ("mdcliv", 1654),
            ("mDxLiX", 1549),
            ("McMxvII", 1917),
        ],
    )
    def test_case_insensitive(
        self,
        converter: RomanConverter,
        insensitive_cases: str,
        expected_arabic: int,
    ) -> None:
        assert (
            converter._standard_converter.to_arabic(insensitive_cases)
            == expected_arabic
        )

    def test_whitespace_handling(self, converter: RomanConverter) -> None:
        assert converter._standard_converter.to_arabic("  MDCLIV  ") == 1654
        assert converter.to_arabic("\tVIII\n") == 8

    def test_type_error_(self, converter: RomanConverter) -> None:
        with pytest.raises(exc.InvalidRomanNumeralError):
            converter._standard_converter.to_arabic(123)  # type:ignore
        with pytest.raises(exc.InvalidRomanNumeralError):
            converter._standard_converter.to_arabic([1, 2, 3])  # type:ignore


class TestExtendedRomanProcessorToRoman:
    @pytest.mark.parametrize(
        "arabic,expected_roman",
        [
            (1, "I"),
            (3999, "MMMCMXCIX"),
            (4000, "IV•"),
            (4004, "IV•IV"),
            (54125, "LIV•CXXV"),
            (17898, "XVII•DCCCXCVIII"),
            (392145, "CCCXCII•CXLV"),
            (49123123, "XLIX••CXXIII•CXXIII"),
            (1000000, "M•"),
        ],
    )
    def test_to_roman_valid(
        self, converter: RomanConverter, arabic: int, expected_roman: str
    ) -> None:
        assert converter._extended_converter.to_roman(arabic) == expected_roman

    @pytest.mark.parametrize(
        "invalid_arabic",
        [
            0,
            -1,
            -1000,
            -999999,
        ],
    )
    def test_to_roman_invalid(
        self, converter: RomanConverter, invalid_arabic: int
    ) -> None:
        with pytest.raises(exc.NumberOutOfRangeError):
            converter._extended_converter.to_roman(invalid_arabic)

    def test_to_roman_large_number(self, converter: RomanConverter) -> None:
        arabic = int(6.022 * 10**23)

        result = converter._extended_converter.to_roman(arabic)
        assert isinstance(result, str)
        assert len(result) > 0
        assert "•" in result


class TestExtendedRomanProcessorToArabic:
    @pytest.mark.parametrize(
        "arabic,expected_roman",
        [
            ("I", 1),
            ("MMMCMXCIX", 3999),
            ("IV•", 4000),
            ("IV•IV", 4004),
            ("LIV•CXXV", 54125),
            ("XVII•DCCCXCVIII", 17898),
            ("CCCXCII•CXLV", 392145),
            ("XLIX••CXXIII•CXXIII", 49123123),
            ("M•", 1000000),
        ],
    )
    def test_to_arabic_valid(
        self, converter: RomanConverter, arabic: str, expected_roman: int
    ) -> None:
        assert converter._extended_converter.to_arabic(arabic) == expected_roman

    @pytest.mark.parametrize(
        "invalid_roman",
        [
            "A",
            "BXI",
            "123",
            "!@#",
            "MMMMM",
            "IL",
            "xm",
            "VX",
            "IVIV",
            "VV",
            "DM",
            "LC",
            "XLXL",
            "CMCM",
            "",
            "   ",
            "\n\t",
            "•IV",
            "IV•A",
        ],
    )
    def test_invalid_roman_raises(
        self, converter: RomanConverter, invalid_roman: str
    ) -> None:
        with pytest.raises(exc.InvalidRomanNumeralError):
            converter._extended_converter.to_arabic(invalid_roman)

    def test_empty_string_raises(self, converter: RomanConverter) -> None:
        with pytest.raises(exc.InvalidRomanNumeralError):
            converter._extended_converter.to_arabic("")

    def test_whitespace_handling(self, converter: RomanConverter) -> None:
        assert converter._extended_converter.to_arabic("  MDCLIV  ") == 1654
        assert converter._extended_converter.to_arabic("\tVIII\n") == 8


class TestValidateExtendedRoman:
    @pytest.mark.parametrize(
        "roman",
        [
            "X",  # Valid single roman numeral
            "X•V",  # Valid extended roman numeral
            "x•v",  # Lowercase, should be accepted after upper()
            "X • V",  # Spaces allowed
            "X\t•\nV",  # Tabs and newlines allowed
            "MCMXCIV",  # Valid standard roman numeral
            "MCMXCIV•",  # Valid with thousand indicator
            "X••V",  # Multiple thousand indicators
        ],
    )
    def test_validate_extended_roman_valid(
        self, converter: RomanConverter, roman: str
    ) -> None:
        converter._extended_converter._validate_extended_roman(roman)

    @pytest.mark.parametrize(
        "roman",
        [
            "X$",  # Invalid character
            "X1",  # Digit not allowed
            "X•V@",  # Special character not allowed
            "abc",  # Non-roman letters
            "X•V#",  # Hash not allowed
            "X•V!",  # Exclamation mark not allowed
            "X•V-",  # Dash not allowed
            "X•V_",  # Underscore not allowed
            "",  # Empty string
        ],
    )
    def test_validate_extended_roman_invalid(
        self, converter: RomanConverter, roman: str
    ) -> None:
        with pytest.raises(exc.InvalidRomanNumeralError):
            converter._extended_converter._validate_extended_roman(roman)


class TestParseRomanGroups:
    @pytest.mark.parametrize(
        "roman,expected",
        [
            ("X", [("X", 0)]),
            ("X•V", [("X", 1), ("V", 0)]),
            ("X••V", [("X", 2), ("V", 0)]),
            ("X•••V", [("X", 3), ("V", 0)]),
            ("X•V•I", [("X", 1), ("V", 1), ("I", 0)]),
            ("X••V•I", [("X", 2), ("V", 1), ("I", 0)]),
            ("X•••", [("X", 3)]),
            ("", [("", 0)]),
            ("X••", [("X", 2)]),
        ],
    )
    def test_parse_roman_groups_valid(
        self, converter: RomanConverter, roman: str, expected: tuple[str, int]
    ) -> None:
        result = converter._extended_converter._parse_roman_groups(roman)
        assert result == expected

    def test_parse_roman_groups_invalid(self, converter: RomanConverter) -> None:
        import src.converters.utils.roman_exceptions as exc

        with pytest.raises(exc.InvalidRomanNumeralError):
            converter._extended_converter._parse_roman_groups("••")


class TestSplitIntoThousands:
    @pytest.mark.parametrize(
        "number,expected",
        [
            (0, [0]),
            (1, [1]),
            (999, [999]),
            (1000, [1_000]),
            (1234, [1_234]),
            (999_999, [999, 999]),
            (1_234_567, [1_234, 567]),
            (4_000, [4, 000]),  ##
            (3_999, [3_999]),
            (4_001, [4, 1]),  ##
            (3_000_001, [3_000, 1]),
            (3_000_003, [3_000, 3]),
            (3_000_004, [3_000, 4]),
            (3_000_003_999, [3_000, 3, 999]),  ##
            (4, [4]),
            (3, [3]),
            (2_003, [2_003]),
            (1_002_003, [1_002, 3]),
        ],
    )
    def test_split_into_thousands(
        self, converter: RomanConverter, number: int, expected: int
    ) -> None:
        result = converter._extended_converter._split_into_thousands(number)
        assert result == expected
