<template>
  <v-dialog
    v-if="_dialog"
    v-model="_dialog"
    width="750"
    persistent
  >
    <component :is="form" @close="_dialog=false"></component>
  </v-dialog>
</template>
<script>
import UserForm from '@/components/forms/UserForm.vue'
import ProjectForm from '@/components/forms/ProjectForm.vue'
import MilestoneForm from '@/components/forms/MilestoneForm.vue'
export default {

  components: {
    UserForm,
    ProjectForm,
    MilestoneForm
  },

  props: {
    dialog: {
      type: Boolean,
      default: false,
    },

    form: {
      type: String,
      default: 'UserForm',
      required: true
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