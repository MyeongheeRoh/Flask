<template>
    <div>
        <!-- Hero -->
        <base-page-heading title="clothes" subtitle="상품 전체 보기">
        <template #extra>
            <b-breadcrumb class="breadcrumb-alt">
            <b-breadcrumb-item href="javascript:void(0)">clothes</b-breadcrumb-item>
            <b-breadcrumb-item active>all</b-breadcrumb-item>
            </b-breadcrumb>
        </template>
        </base-page-heading>
        <!-- END Hero -->
        <!-- Page Content -->
        <div class="content">
        <!-- Simple Ribbon -->
        <h2 class="content-heading">All</h2>
        <b-row>
            <div v-for="(product, index) in products" :key="index">   
            <b-col class="flexbox" md="4" xl="3">
            <!-- Bottom Right Primary -->
            <base-block rounded :ribbon="product.cost_price" ribbon-variant="dark" ribbon-bottom>
                <div class="text-center py-4 push">
                <p>
                    <i class="fab fa-3x fa-html5 text-gray"></i>
                </p>
                <img class="productImg" :src=" '/img/' + product.img_address">
                </div>
            </base-block>
            <!-- END Bottom Right Primary -->
            </b-col>
            </div>
        </b-row>
        </div>
        <!-- END Page Content -->
    </div>
</template>

<script>
import axios from 'axios'

export default {
    data(){
        return {
            products: {},
        };
    },
    methods: {
        getProducts(){
            axios.get('http://localhost:5000/product')
            .then((res) => {
                this.products = res.data.products;
                console.log('success');
            })
            .catch((error) => {
                console.error(error);
            });
        },
    },
    created(){
        this.getProducts();
    },
}
</script>