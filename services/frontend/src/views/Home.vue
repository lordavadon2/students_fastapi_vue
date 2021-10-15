<template>
  <div>
    <h6 class="card text-white bg-primary mb-1">Manage your students</h6>
    <div class="card-body">
      <h5 class="text-white bg-dark">Add your student</h5>
      <span class="card-text">
        <form @submit.prevent="addStudent">
          <input
            v-model="student.name"
            type="text"
            class="form-card stud-name mb-2 col2"
            placeholder="Enter name"
          />
          <input
            v-model="student.email"
            type="text"
            class="form-card stud-email mb-2 col2"
            placeholder="Enter email"
          />
          <input
            v-model="student.phone"
            type="text"
            class="form-card stud-phone mb-2 col2"
            placeholder="Enter phone"
          />
          <button
            type="submit"
            class="btn btn-outline-warning mb-2"
            style="font-weight: bold;"
          >
            Add student
          </button>
        </form>
      </span>
      <h5 class="card text-white bg-primary mb-1">Your student</h5>
      <div class="row row-cols-1 row-cols-md-2 g-4">
        <student-component
          v-for="student in studentList"
          :key="student._id"
          :student="student"
          @delete="deleteStudent"
        />
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import StudentComponent from '@/components/StudentComponent'

export default {
  name: 'Home',
  components: {StudentComponent},
  data() {
    return {
      studentList: [],
      student: {
        name: '',
        email: '',
        phone: ''
      }
    }
  },
  methods: {
    getStudents() {
      axios
        .get('/students')
        .then(response => {
          this.studentList = response.data
        })
        .catch(error => {
          console.log(error)
        })
    },
    addStudent() {
      const newStudent = {
        name: this.student.name,
        email: this.student.email,
        phone: this.student.phone
      }
      axios
        .post('/students', newStudent)
        .then(response => {
          this.getStudents()
          alert('Student added to list!')
        })
        .catch(error => {
          console.log(error)
        })
      this.clearStudent()
    },
    clearStudent() {
      this.student.name = ''
      this.student.email = ''
      this.student.phone = ''
    },
    deleteStudent(id) {
      axios
        .delete(`/students/${id}`)
        .then(response => {
          this.getStudents()
          alert('Student deleted from list!')
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  mounted() {
    this.getStudents()
  }
}
</script>
