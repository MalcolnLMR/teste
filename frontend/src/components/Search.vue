<template>
  <div class="search-container">
    <h1>Busca de Operadoras</h1>
    <div class="search-bar">
      <input v-model="query" @input="search" placeholder="Digite o nome da operadora..." />
    </div>
    <div class="results-table">
      <table v-if="results.length">
        <thead>
          <tr>
            <th>Nome Fantasia</th>
            <th>Razão Social</th>
            <th>Registro ANS</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="operadora in results" :key="operadora.Registro_ANS">
            <td>{{ operadora.Nome_Fantasia }}</td>
            <td>{{ operadora.Razao_Social }}</td>
            <td>{{ operadora.Registro_ANS }}</td>
          </tr>
        </tbody>
      </table>
      <p v-else>Nenhum resultado encontrado.</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      query: '',
      results: [],
    };
  },
  methods: {
    async search() {
      if (this.query.length > 2) {
        const response = await axios.get(`http://127.0.0.1:8000/search?q=${this.query}`);
        this.results = response.data;
      } else {
        this.results = [];
      }
    },
  },
};
</script>

<style scoped>
.search-container {
  margin: 0 auto;
  padding: 20px;
}

.search-bar {
  position: sticky;
  top: 0;
  background-color: white;
  width: 100%;
  box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
  z-index: 1000;
}

input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.results-table {
  width: 100%;
  margin-top: 20px;
  overflow-x: auto;
}

table {
  width: 100%;
  border-collapse: collapse;
  color: #ececec;
}

th, td {
  text-align: left;
  padding: 10px;
  border: 1px solid #ddd;
}

th {
  background-color: #383838;
}

tr:nth-child(even) {
  background-color: #383838;
}
</style>