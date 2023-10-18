"""Main module of Finance Application"""
from typing import List
from fastapi import FastAPI, HTTPException

from finance_project.models.stocks import Stock

from finance_project.schemas.stock_schemas import StockSchema


app = FastAPI()


stocks: List[Stock] = [
        Stock("Apple Company", 102, "AAPL.US"),
        Stock("Google Company", 78, "GOOG.US"),
        Stock("Microsoft Company", 92, "MSFT.US"),
    ]


@app.get("/stocks")
def get_stocks():
    return stocks


@app.post("/stocks/create-stock")
def create_stock(stock_body: StockSchema):
    stock = Stock(**stock_body.model_dump())
    stocks.append(stock)


@app.get("/stocks/{name}")
def read_item(name: str):
    for stock in stocks:
        if stock.name == name:
            return stock
    raise HTTPException(status_code=404, detail="Company doesn't exists")
