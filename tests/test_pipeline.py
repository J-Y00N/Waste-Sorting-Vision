from waste_sorting_vision.pipeline import summarize_class_counts


def test_summarize_class_counts_sorts_by_count_then_name() -> None:
    class_names = {
        0: "Paper",
        1: "Can",
        2: "Battery",
    }

    summary = summarize_class_counts([1, 0, 1, 2, 2], class_names)

    assert list(summary.items()) == [
        ("Battery", 2),
        ("Can", 2),
        ("Paper", 1),
    ]
