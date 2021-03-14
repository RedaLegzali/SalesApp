<template>
  <Header />
  <div class="container mt-5">
    <nav class="breadcrumb" aria-label="breadcrumbs">
      <ul>
        <li><router-link to="/">Home</router-link></li>
        <li><a @click="back()">Products</a></li>
        <li class="is-active">
          <a href="#" aria-current="page">Skus</a>
        </li>
      </ul>
    </nav>
    <h1 class="title">Skus</h1>
    <div id="skus">
      <div v-for="sku in skus" :key="sku.id">
        <Sku
          :id="sku.id"
          :original="sku.original"
          :price="sku.price"
          :quantity="sku.quantity"
          :name="sku.name"
          :image="sku.image"
        />
      </div>
    </div>
  </div>
</template>

<script>
import Header from '@/components/Header.vue';
import Sku from '@/components/Sku.vue';

export default {
  name: 'Skus',
  data() {
    return {
      id: this.$route.params.id,
      skus: Array
    };
  },
  components: {
    Header,
    Sku
  },
  methods: {
    back() {
      this.$router.go(-1);
    }
  },
  async mounted() {
    const resp = await fetch(
      `${process.env.VUE_APP_FURNITURES}/skus/${this.id}`
    );
    const data = await resp.json();
    this.skus = data;
  }
};
</script>

<style scoped>
#skus {
  display: flex;
  justify-content: space-around;
  flex-direction: row;
  flex-wrap: wrap;
}
</style>
