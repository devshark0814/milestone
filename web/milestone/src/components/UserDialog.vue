<template>
  <v-dialog
    v-if="_dialog"
    v-model="_dialog"
    width="750"
  >
    <UserForm @close="_dialog=false" />
  </v-dialog>
</template>
<script>
import UserForm from '@/components/forms/UserForm.vue'
export default {

  components: {
    UserForm
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