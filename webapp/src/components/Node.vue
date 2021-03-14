<template>
  <router-link
    class="button is-link is-inverted"
    :to="{ name: 'Product', params: { id: id } }"
    >{{ name }}</router-link
  >
</template>

<script>
export default {
  name: 'Node',
  props: {
    id: Number,
    name: String
  }
};
</script>
