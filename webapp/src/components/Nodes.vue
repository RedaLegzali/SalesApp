<template>
  <h1 class="title">Nodes</h1>
  <div v-for="node in nodes" :key="node.id">
    <Node :id="node.id" :name="node.name" />
  </div>
</template>

<script>
import Node from '@/components/Node';
export default {
  name: 'Nodes',
  components: { Node },
  props: {
    channel_id: Number
  },
  watch: {
    channel_id() {
      this.fetchNodes();
    }
  },
  data() {
    return {
      nodes: Array
    };
  },
  methods: {
    async fetchNodes() {
      try {
        let resp = await fetch(
          `${process.env.VUE_APP_FURNITURES}/nodes/${this.channel_id}`
        );
        let data = await resp.json();
        this.nodes = data;
      } catch (err) {
        console.log(err);
      }
    }
  },
  mounted() {
    this.fetchNodes();
  }
};
</script>
