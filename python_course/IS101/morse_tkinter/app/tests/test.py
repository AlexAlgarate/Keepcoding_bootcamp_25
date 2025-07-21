import tkinter as tk

import pytest

from ..views import AppButton


@pytest.fixture
def root():
    root = tk.Tk()
    root.withdraw()  # oculta la ventana
    yield root
    root.destroy()


@pytest.mark.parametrize(
    "label, num_clicks, result",
    [
        ("1", 3, ["1"] * 3),
        ("clear", 1, ["clear"]),
    ],
)
def test_AppButton_clicked(root, label, num_clicks, result):
    clicks = []

    button = AppButton(root, label, lambda label: clicks.append(label))
    for _ in range(num_clicks):
        button.click()
    assert clicks == result
