<template>
    <div class="container">
        <div class="row">
            <div class="col-sm-10">
                <h1>Usuarios</h1>
                <hr><br><br>
                <button type="button" class="btn btn-success btn-sm">Agregar Usuarios</button>
                <br><br>
                <table class="table table-hover">
                    <thead>
                    <tr>
                        <th scope="col">Nombre</th>
                        <th scope="col">Apellidos</th>
                        <th scope="col">Telefono</th>
                        <th scope="col">Correo</th>
                        <th></th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr v-for="(usuario, index) in usuarios" :key="index">
                        <td>{{ usuario.nombre }}</td>
                        <td>{{ usuario.apellidos }}</td>
                        <td>
                            <span v-if="book.read">Yes</span>
                            <span v-else>No</span>
                        </td>
                        <td>
                            <div class="btn-group" role="group">
                                <button type="button" class="btn btn-warning btn-sm">Update</button>
                                <button type="button" class="btn btn-danger btn-sm">Delete</button>
                            </div>
                        </td>
                    </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      usuarios: [],
    };
  },
  methods: {
    getUsuarios() {
      const path = 'http://localhost:5000/usuarios';
      axios.get(path)
        .then((res) => {
          this.usuarios = res.data.usuarios;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getUsuarios();
  },
};
</script>
