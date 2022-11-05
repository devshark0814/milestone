<template>
  <v-dialog
    v-if="_dialog"
    v-model="_dialog"
    width="750"
    style="z-index: 999;"
  >
    <PjForm @close="_dialog=false" />
  </v-dialog>
</template>
<script>
import PjForm from '@/components/forms/PjForm.vue'
export default {

  components: {
    PjForm
  },

  props: {
    dialog: {
      type: Boolean,
      default: false,
    }
  },

  data() {
    return {
    }
  },

  computed: {
    _dialog: {
      get() {
        return this.dialog
      },
      set(v) {
        this.$emit('close', v)
      }
    }
  },
}
</script>