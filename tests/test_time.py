import pytest

from swinlib.time import time_float_to_datetime, datetime_string_to_time_float

@pytest.mark.parametrize(
    "swin_time_string,swin_time_float",
    [
        ("2018-12-11, 16:37:35", 566239055.0),
        ("2025-02-05, 21:37:09", 760484229.379076),
        ("2025-03-02, 10:02:14", 762602534.625131),
    ]
)
def test_float_to_time(swin_time_string, swin_time_float):
    t1 = time_float_to_datetime(swin_time_float)
    assert swin_time_string == t1.strftime("%Y-%m-%d, %H:%M:%S")

@pytest.mark.parametrize(
    "swin_time_string,swin_time_float",
    [
        ("2018-12-11, 16:37:35", 566239055.0),
        ("2025-02-05, 21:37:09", 760484229.379076),
        ("2025-03-02, 10:02:14", 762602534.625131),
    ]
)
def test_time_to_float(swin_time_string, swin_time_float):
    t1 = datetime_string_to_time_float(swin_time_string)
    assert (swin_time_float - t1) < 1
