import os
from flask import render_template, request, Flask
from clothesmall.database import dao
from clothesmall.model.product import Product


@app.route('/')
def register_product_form():
    '''상품 등록을 위한 폼을 제공하는 함수'''
    print('상품 등록')
    return render_template('registerproduct.html')
