import pytest

from main import (
    InvalidRomanNumeralError,
    NumberOutOfRangeError,
    RomanCalculator,
    RomanNumeralValidator,
    create_roman_calculator,
)


@pytest.fixture
def calculator() -> RomanCalculator:
    return create_roman_calculator()


class TestRomanCalculatorArabicToRoman:
    @pytest.mark.parametrize(
        "input_values,expected_values",
        [
            (1, "I"),
            (2, "II"),
            (3, "III"),
            (4, "IV"),
            (5, "V"),
            (9, "IX"),
            (10, "X"),
            (27, "XXVII"),
            (48, "XLVIII"),
            (59, "LIX"),
            (93, "XCIII"),
            (141, "CXLI"),
            (163, "CLXIII"),
            (402, "CDII"),
            (575, "DLXXV"),
            (911, "CMXI"),
            (1024, "MXXIV"),
            (1234, "MCCXXXIV"),
            (1549, "MDXLIX"),
            (3000, "MMM"),
            (3999, "MMMCMXCIX"),
        ],
    )
    def test_valid_conversions_arabic_to_roman(
        self, calculator: RomanCalculator, input_values: int, expected_values: str
    ) -> None:
        assert (
            calculator._from_arabic_smaller_4000_to_roman(input_values)
            == expected_values
        )

    @pytest.mark.parametrize(
        "invalid_number",
        [0, -1, -10, 4000, 4001, 10000],
    )
    def test_invalid_conversions_arabic_to_roman(
        self, calculator: RomanCalculator, invalid_number: int
    ) -> None:
        with pytest.raises(
            NumberOutOfRangeError,
            match="El número tiene que estar entre 1 y 3999.",
        ):
            calculator._from_arabic_smaller_4000_to_roman(invalid_number)


class TestRomanCalculatorRomantoArabic:
    @pytest.mark.parametrize(
        "expected_values,input_values",
        [
            (1, "I"),
            (2, "II"),
            (3, "III"),
            (4, "IV"),
            (5, "V"),
            (9, "IX"),
            (10, "X"),
            (27, "XXVII"),
            (48, "XLVIII"),
            (59, "LIX"),
            (93, "XCIII"),
            (141, "CXLI"),
            (163, "CLXIII"),
            (402, "CDII"),
            (575, "DLXXV"),
            (911, "CMXI"),
            (1024, "MXXIV"),
            (1234, "MCCXXXIV"),
            (1549, "MDXLIX"),
            (3000, "MMM"),
            (3999, "MMMCMXCIX"),
        ],
    )
    def test_valid_conversions_roman_to_arabic(
        self, calculator, input_values: int, expected_values: str
    ) -> None:
        assert (
            calculator.from_roman_smaller_4000_to_arabic(input_values)
            == expected_values
        )

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
        ],
    )
    def test_invalid_roman_numerals(
        self, calculator: RomanCalculator, invalid_roman: str
    ) -> None:
        with pytest.raises(InvalidRomanNumeralError, match="Número romano no válido"):
            calculator.from_roman_smaller_4000_to_arabic(invalid_roman)

    def test_whitespace_only_string(self, calculator: RomanCalculator) -> None:
        with pytest.raises(InvalidRomanNumeralError) as exctype:
            calculator.from_roman_smaller_4000_to_arabic("   ")
            assert "Cadena romana vacía" == exctype.value

    def test_empty_string(self, calculator: RomanCalculator) -> None:
        with pytest.raises(InvalidRomanNumeralError) as exctype:
            calculator.from_roman_smaller_4000_to_arabic("")
            assert "Cadena romana vacía" == exctype.value

    @pytest.mark.parametrize(
        "insensitive_cases,expected_arabics",
        [
            ("mdxlix", 1549),
            ("mDxLiX", 1549),
            ("MdXlix", 1549),
        ],
    )
    def test_case_insensitive_roman_to_arabic(
        self, calculator: RomanCalculator, insensitive_cases: str, expected_arabics: int
    ) -> None:
        assert (
            calculator.from_roman_smaller_4000_to_arabic(insensitive_cases)
            == expected_arabics
        )

    def test_whitespace_handling(self, calculator: RomanCalculator):
        assert calculator.from_roman_smaller_4000_to_arabic("  MDXLIX  ") == 1549
        assert calculator.from_roman_smaller_4000_to_arabic("\tVIII\n") == 8


class TestRomanCalculatorIsValidRoman:
    def test_raise_exception_when_you_try_to_modify_dictionaries(
        self, calculator: RomanCalculator
    ):
        with pytest.raises(TypeError) as exc:
            calculator._arabic_to_roman_map[123] = "123"  # type: ignore

            calculator._from_arabic_smaller_4000_to_roman(123)
            assert "'mappingproxy' object does not support item assignment" == exc.value


class TestRomanCalculatorRoundTrip:
    @pytest.mark.parametrize(
        "non_used_input,expected_roman",
        [
            (1, "I"),
            (2, "II"),
            (3, "III"),
            (4, "IV"),
            (5, "V"),
            (9, "IX"),
            (10, "X"),
            (27, "XXVII"),
            (48, "XLVIII"),
            (59, "LIX"),
            (93, "XCIII"),
            (141, "CXLI"),
            (163, "CLXIII"),
            (402, "CDII"),
            (575, "DLXXV"),
            (911, "CMXI"),
            (1024, "MXXIV"),
            (1234, "MCCXXXIV"),
            (1549, "MDXLIX"),
            (3000, "MMM"),
            (3999, "MMMCMXCIX"),
        ],
    )
    def test_roman_to_arabic_to_roman(
        self, calculator: RomanCalculator, expected_roman: str, non_used_input: int
    ) -> None:
        number = calculator.from_roman_smaller_4000_to_arabic(expected_roman)
        result = calculator._from_arabic_smaller_4000_to_roman(number)
        assert result == expected_roman

    @pytest.mark.parametrize(
        "expected_arabic, non_used_roman",
        [
            (1, "I"),
            (2, "II"),
            (3, "III"),
            (4, "IV"),
            (5, "V"),
            (9, "IX"),
            (10, "X"),
            (27, "XXVII"),
            (48, "XLVIII"),
            (59, "LIX"),
            (93, "XCIII"),
            (141, "CXLI"),
            (163, "CLXIII"),
            (402, "CDII"),
            (575, "DLXXV"),
            (911, "CMXI"),
            (1024, "MXXIV"),
            (1234, "MCCXXXIV"),
            (1549, "MDXLIX"),
            (3000, "MMM"),
            (3999, "MMMCMXCIX"),
        ],
    )
    def test_arabic_to_roman_to_arabic(
        self, calculator: RomanCalculator, expected_arabic: int, non_used_roman: str
    ) -> None:
        roman = calculator._from_arabic_smaller_4000_to_roman(expected_arabic)
        result = calculator.from_roman_smaller_4000_to_arabic(roman)
        assert result == expected_arabic


class TestRomanCalculatorLargeArabics:
    @pytest.mark.parametrize(
        "input_arabic, expected_roman",
        [
            (
                int(6.022 * 10**23),
                "DCII•••••••CXCIX••••••CMXCIX•••••CMXCIX••••CMXCIX•••CMLX••CLIV•CXII",
            ),
            (49123123, "XLIX••CXXIII•CXXIII"),
            (54125, "LIV•CXXV"),
            (4004, "IV•IV"),
            (17898, "XVII•DCCCXCVIII"),
            (392145, "CCCXCII•CXLV"),
            # (3999999, "MMMCMXCIX•CMXCIX"),
        ],
    )
    def test_valid_large_numbers(
        self, calculator: RomanCalculator, input_arabic: int, expected_roman: str
    ) -> None:
        assert calculator.from_arabic_to_roman(input_arabic) == expected_roman


class TestRomanCalculatorLargeRomans:
    @pytest.mark.parametrize(
        "input_roman,expected_number",
        [
            (
                "DCII•••••••CXCIX••••••CMXCIX•••••CMXCIX••••CMXCIX•••CMLX••CLIV•CXII",
                int(6.022 * 10**23),
            ),
            ("XLIX••CXXIII•CXXIII", 49123123),
            ("LIV•CXXV", 54125),
            ("IV•IV", 4004),
            ("XVII•DCCCXCVIII", 17898),
            ("CCCXCII•CXLV", 392145),
        ],
    )
    def test_valid_large_romans(
        self, calculator: RomanCalculator, input_roman: str, expected_number: int
    ) -> None:
        assert calculator.from_roman_to_arabic(input_roman) == expected_number


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
        with pytest.raises(NumberOutOfRangeError, match="El número debe ser numérico"):
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
        with pytest.raises(NumberOutOfRangeError, match="El número debe ser entero"):
            validator.validate_arabic_input(invalid_arabic_float)

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
            "XLIX••CXXIII•CXXIII",
            "LIV•CXXV",
            "IV•IV",
            "XVII•DCCCXCVIII",
            "CCCXCII•CXLV",
            "ix",
            "MdCXvI",
        ],
    )
    def test_valid_type_for_roman(
        self, calculator: RomanCalculator, roman: str
    ) -> None:
        assert isinstance(calculator._validate_roman_string(roman), str)

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
        self, calculator: RomanCalculator, roman: str
    ) -> None:
        with pytest.raises(
            InvalidRomanNumeralError, match="El valor debe ser una cadena de texto"
        ):
            calculator._validate_roman_string(roman)

    @pytest.mark.parametrize(
        "invalid_input",
        [
            "",
            "   ",
            "\n\t",
        ],
    )
    def test_invalid_empty_string(
        self, calculator: RomanCalculator, invalid_input: str
    ) -> None:
        with pytest.raises(
            InvalidRomanNumeralError, match="Cadena romana vacía."
        ) as excinfo:
            calculator._validate_roman_string(invalid_input)
            assert "Cadena romana vacía." == excinfo.value
