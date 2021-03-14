<template>
  <button
    :id="id"
    @click="selectChannel(id)"
    class="ml-5 button is-rounded is-outlined"
  >
    {{ name }}
  </button>
</template>

<script>
export default {
  name: 'Channel',
  props: {
    id: Number,
    name: String
  },
  methods: {
    selectChannel(id) {
      const buttons = document.getElementsByTagName('button');
      buttons.forEach(button => {
        button.classList.remove('is-primary');
      });
      const button = document.getElementById(id);
      button.classList.add('is-primary');
      this.$emit('showNodes', id);
    }
  }
};
</script>
