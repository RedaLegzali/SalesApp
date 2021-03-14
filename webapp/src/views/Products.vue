<template>
  <Header />
  <div class="container mt-5">
    <nav class="breadcrumb" aria-label="breadcrumbs">
      <ul>
        <li><router-link to="/">Home</router-link></li>
        <li class="is-active">
          <a href="#" aria-current="page">Products</a>
        </li>
      </ul>
    </nav>
    <h1 class="title">Products</h1>
    <div id="products">
      <div v-for="product in products" :key="product.id">
        <Product :id="product.id" :name="product.name" :image="product.image" />
      </div>
    </div>
  </div>
</template>

<script>
import Header from '@/components/Header.vue';
import Product from '@/components/Product.vue';

export default {
  name: 'Products',
  data() {
    return {
      id: this.$route.params.id,
      products: Array
    };
  },
  components: {
    Header,
    Product
  },
  async mounted() {
    const resp = await fetch(
      `${process.env.VUE_APP_FURNITURES}/products/${this.id}`
    );
    const data = await resp.json();
    this.products = data;
  }
};
</script>

<style scoped>
#products {
  display: flex;
  justify-content: space-around;
  flex-direction: row;
  flex-wrap: wrap;
}
</style>
