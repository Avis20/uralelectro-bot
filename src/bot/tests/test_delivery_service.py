import pytest
from bot.services.delivery_service import DeliveryService
from bot.tests.testdata.delivery_test_data import DeliveryTestData


@pytest.mark.asyncio
async def test_calculate_delivery_cost():
    # Arrange
    test_data = DeliveryTestData.get_valid_data()
    
    # Act
    result = await DeliveryService.calculate_delivery_cost(
        price=test_data["price"],
        quantity=test_data["quantity"],
        address=test_data["address"]
    )
    
    # Assert
    assert result.product_price == test_data["expected"].product_price
    assert result.delivery_price == test_data["expected"].delivery_price
    assert result.vat_price == test_data["expected"].vat_price
    assert result.total_price == test_data["expected"].total_price


@pytest.mark.asyncio
async def test_calculate_delivery_cost_with_zero_quantity():
    # Arrange
    test_data = DeliveryTestData.get_zero_quantity_data()
    
    # Act
    result = await DeliveryService.calculate_delivery_cost(
        price=test_data["price"],
        quantity=test_data["quantity"],
        address=test_data["address"]
    )
    
    # Assert
    assert result.product_price == test_data["expected"].product_price
    assert result.delivery_price == test_data["expected"].delivery_price
    assert result.vat_price == test_data["expected"].vat_price
    assert result.total_price == test_data["expected"].total_price


@pytest.mark.asyncio
async def test_calculate_delivery_cost_with_negative_quantity():
    # Arrange
    test_data = DeliveryTestData.get_negative_quantity_data()
    
    # Act & Assert
    with pytest.raises(ValueError):
        await DeliveryService.calculate_delivery_cost(
            price=test_data["price"],
            quantity=test_data["quantity"],
            address=test_data["address"]
        )


@pytest.mark.asyncio
async def test_calculate_delivery_cost_with_negative_price():
    # Arrange
    test_data = DeliveryTestData.get_negative_price_data()
    
    # Act & Assert
    with pytest.raises(ValueError):
        await DeliveryService.calculate_delivery_cost(
            price=test_data["price"],
            quantity=test_data["quantity"],
            address=test_data["address"]
        )
