<template>
  <div class="card">
    <header class="card-header">
      <router-link
        class="card-header-title button"
        :to="{ name: 'Skus', params: { id: id } }"
      >
        {{ name }}
      </router-link>
    </header>
    <div class="card-image">
      <figure class="image">
        <img :src="require(`@/assets/images/products/${image}`)" :alt="name" />
      </figure>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Product',
  props: {
    id: Number,
    name: String,
    image: String
  }
};
</script>

<style scoped>
img {
  width: 300px;
  height: 300px;
}
.card {
  width: 300px;
}
</style>
