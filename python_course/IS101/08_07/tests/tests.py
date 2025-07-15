import pytest

from main import (
    InvalidRomanNumeralError,
    NumberOutOfRangeError,
    RomanCalculator,
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
    @pytest.mark.parametrize(
        "valid_roman",
        ["III", "III", "IV", "V", "IX", "X", "XXVII", "XLVIII", "LIX", "XCIII"],
    )
    def test_valid_roman_patterns(
        self, calculator: RomanCalculator, valid_roman: str
    ) -> None:
        assert calculator.is_valid_roman(valid_roman)

    @pytest.mark.parametrize(
        "invalid_roman", ["IIII", "VV", "LL", "DD", "IC", "IM", "XM", "MMMM"]
    )
    def test_invalid_roman_patterns(self, invalid_roman):
        assert RomanCalculator.is_valid_roman(invalid_roman) is False

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
