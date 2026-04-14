from waste_sorting_vision.class_names import get_class_name, load_class_names


def test_class_names_loads_expected_mapping() -> None:
    class_names = load_class_names()
    assert class_names[0] == "Paper"
    assert class_names[15] == "Battery"
    assert len(class_names) == 16


def test_unknown_class_name_uses_safe_fallback() -> None:
    assert get_class_name(99, {0: "Paper"}) == "class_99"
