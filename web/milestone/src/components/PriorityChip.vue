<template>
  <v-chip
    label
    :color="priorityColor(priority)"
    :text-color="priorityTextColor(priority)"
  >
    {{ priorityName(priority) }}
  </v-chip>
</template>
<script>
export default {

  props: {
    priority: {
      type: Number,
      default: 0
    }
  },

  computed: {
    priorityName: (v) => {
      return (v) => {
        switch (v) {
          case 1:
            return '低め'
          case 2:
            return '可能なら'
          case 3:
            return '通常'
          case 4:
            return '高め'
          default:
            return '緊急'
        }
      }
    },
    priorityColor: (v) => {
      return (v) => {
        if(v==4) return 'orange lighten'
        if(v==5) return 'red darken-1'
        return 'light-blue lighten-5'
      }
    },
    priorityTextColor: (v) => {
      return (v) => {
        if(v==4 || v==5) return 'white'
        return 'light-blue darken-1'
      }
    },
  }
}
</script>