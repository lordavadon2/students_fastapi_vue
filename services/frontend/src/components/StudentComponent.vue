<template>
  <div class="col">
    <div class="card">
      <div class="card-body">
        <h5 class="card-title">{{ student.name }}</h5>
        <p class="card-text">{{ student.email }}</p>
        <small class="text-muted">{{ student.phone }}</small>
      </div>
      <div class="mb-2">
        <button class="btn btn-danger" @click="deleteStudent">
          Delete
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'StudentComponent',
  props: {
    student: {
      type: Object,
      required: true
    }
  },
  methods: {
    deleteStudent() {
      this.$emit('delete', this.student.id)
    }
  }
}
</script>
