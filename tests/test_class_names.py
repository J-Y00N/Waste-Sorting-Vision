from waste_sorting_vision.class_names import get_class_name, load_class_names


def test_best5_class_names_load_expected_mapping() -> None:
    class_names = load_class_names("best5")
    assert class_names[0] == "Paper"
    assert class_names[15] == "Battery"
    assert len(class_names) == 16


def test_best_class_names_load_expected_mapping() -> None:
    class_names = load_class_names("best")
    assert class_names[0] == "paper"
    assert class_names[14] == "foam + f_s"
    assert len(class_names) == 15


def test_unknown_class_name_uses_safe_fallback() -> None:
    assert get_class_name(99, {0: "Paper"}) == "class_99"
