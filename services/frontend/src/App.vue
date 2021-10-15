<template>
  <div class="container">
    <div
      class="list-group-item justify-content-center align-items-center mx-auto mt-3 text-center"
      style="width: 80vw; background-color: #fff;"
    >
      <h2 class="card text-white bg-primary mb-1 ">
        School Management System
      </h2>
        <router-view />
      </div>
      <h6 class="card text-dark text-center bg-warning">
        All rights reserved &copy; 2021
      </h6>
    </div>
  </div>
</template>

<style>
.col2 {
  width: 100%;
}
</style>
