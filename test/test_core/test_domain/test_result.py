
import pytest
import asyncio

from core.domain.failure import Failure
from core.domain.result import Result


# --- Mock functions for testing composition ---
def sync_to_upper(text: str) -> str:
    return text.upper()

def sync_divide_by_two(n: int) -> Result[float]:
    if n == 0:
        return Result.fail("Cannot divide zero")
    return Result.success(n / 2)

async def async_fetch_data(id: int) -> Result[str]:
    await asyncio.sleep(0.01)  # Simulate IO
    if id == 404:
        return Result.fail("Not found")
    return Result.success(f"data_{id}")

# --- Tests ---
def test_result_success_initialization():
    res = Result.success("hello")
    assert res.is_success is True
    assert res.unwrap() == "hello"

def test_result_failure_initialization():
    res = Result.fail("error")
    assert res.is_success is False
    assert isinstance(res.failure(), Failure)
    assert res.failure().message == "error"

def test_map_transforms_value_on_success():
    res = Result.success("hello").map(sync_to_upper)
    assert res.unwrap() == "HELLO"

def test_map_skipped_on_failure():
    # If it starts as a failure, map should just pass the failure through
    res = Result.fail("initial error").map(sync_to_upper)
    assert res.is_success is False
    assert res.failure().message == "initial error"

def test_bind_chains_results():
    res = Result.success(10).bind(sync_divide_by_two)
    assert res.unwrap() == 5.0

def test_bind_returns_failure_from_func():
    res = Result.success(0).bind(sync_divide_by_two)
    assert res.is_success is False
    assert res.failure().message == "Cannot divide zero"

@pytest.mark.asyncio
async def test_async_bind_success():
    res = await Result.success(1).async_bind(async_fetch_data)
    assert res.unwrap() == "data_1"

@pytest.mark.asyncio
async def test_async_bind_failure_propagation():
    # Start with a success, but the async function returns a failure
    res = await Result.success(404).async_bind(async_fetch_data)
    assert res.is_success is False
    assert res.failure().message == "Not found"

@pytest.mark.asyncio
async def test_async_bind_skips_if_already_failed():
    # If the chain is already failed, the async function should never even run
    res = await Result.fail("stop here").async_bind(async_fetch_data)
    assert res.failure().message == "stop here"