<template>
  <Header />
  <div class="mt-5 container">
    <Channels @showNodes="showNodes" />
  </div>
  <div v-if="nodes" class="mt-5 container">
    <Nodes :channel_id="channel_id" />
  </div>
</template>

<script>
import Header from '@/components/Header.vue';
import Channels from '@/components/Channels.vue';
import Nodes from '@/components/Nodes.vue';

export default {
  name: 'Home',
  components: { Header, Channels, Nodes },
  data() {
    return {
      nodes: false,
      channel_id: null
    };
  },
  methods: {
    showNodes(id) {
      this.nodes = true;
      this.channel_id = id;
    }
  }
};
</script>
