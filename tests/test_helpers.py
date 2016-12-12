# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pytest
import types
from rakuten_ws.webservice import RakutenWebService
from rakuten_ws.base import RakutenAPIResponse


@pytest.mark.online
def test_response(credentials):
    ws = RakutenWebService(**credentials)
    response = ws.ichiba.item.search(keyword="Naruto")
    assert isinstance(response, RakutenAPIResponse)


@pytest.mark.online
def test_single_item(credentials):
    ws = RakutenWebService(**credentials)
    response = ws.ichiba.item.search(keyword="Naruto")
    item = response['Items'][0]
    assert item['itemName'] == 'NARUTO THE BEST (期間生産限定盤) [ (アニメーション) ]'  # noqa


@pytest.mark.online
def test_item_pages(credentials):
    ws = RakutenWebService(**credentials)
    response = ws.ichiba.item.search(keyword="Naruto")
    items = response.pages()
    # search should also allow to retrieve all the available responses
    # within a generator
    assert isinstance(items, types.GeneratorType)
    # The iteration should switch to the next page
    assert next(items)['page'] == 1
    assert next(items)['page'] == 2
