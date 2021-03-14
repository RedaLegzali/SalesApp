<template>
  <h1 class="title">Channels</h1>
  <div v-for="channel in channels" :key="channel.id" class="container buttons">
    <Channel
      :id="channel.id"
      :name="channel.name"
      @showNodes="$emit('showNodes', channel.id)"
    />
  </div>
</template>

<script>
import Channel from '@/components/Channel';
export default {
  name: 'Channels',
  components: { Channel },
  data() {
    return {
      channels: Array
    };
  },
  async mounted() {
    try {
      let resp = await fetch(`${process.env.VUE_APP_FURNITURES}/channels`);
      let data = await resp.json();
      this.channels = data;
    } catch (err) {
      console.log(err);
    }
  }
};
</script>

<style scoped>
div {
  display: inline-block;
}
</style>
