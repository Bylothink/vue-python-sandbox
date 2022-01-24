<template>
  <div class="container">
    <h1 style="margin-top: 1em;">Web Python Sandbox</h1>
    <hr />
    <div v-if="isInError"
         class="alert alert-danger"
         role="alert">
      <h3 class="alert-heading">
        Si è verificato un errore!
      </h3>
      Controlla il codice che hai scritto;
      potresti trovarci un piccolo errore.<br />
      Sei sicuro di aver passato il numero giusto di parametri?
      <div v-if="errorMessage">
        <hr />
        <pre>{{ errorMessage }}</pre>
      </div>
    </div>
    <form @submit.prevent="runApplication">
      <div style="margin-bottom: 1em; text-align: right;">
        <button class="btn btn-success btn-sm"
                type="button"
                @click="addField">
          Aggiungi campo
        </button>
        <button class="btn btn-danger btn-sm"
                style="margin-left: 0.5em;"
                type="button"
                @click="deleteField">
          Rimuovi campo
        </button>
      </div>
      <div v-for="index in range(numberOfFields)"
           :key="`field_${index}`"
           class="form-group row mb-2">
        <label :for="`field_${index}`" class="col-sm-2 col-form-label">
          Parametro #{{ index + 1 }}:
        </label>
        <div class="col-sm-10">
          <input :id="`field_${index}`" class="form-control" />
        </div>
      </div>
      <hr />
      <button class="btn btn-primary btn-lg">Esegui</button>
      <button class="btn btn-secondary btn-lg"
              @click="reset"
              style="margin-left: 0.5em;"
              type="button">
        Reset
      </button>
    </form>
    <hr />
    <table class="table table-bordered table-hover table-striped" style="margin: 1em 0px;">
      <thead>
        <tr>
          <th v-for="cell, index in headers" :key="`header_${index}`">
            {{ cell }}
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="row, i in data" :key="`row_${i}`">
          <td v-for="cell, j in row" :key="`cell_${i}_${j}`">
            {{ cell }}
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
  import axios from 'axios';
  import { ref } from 'vue';

  function* range(value)
  {
    for (let index = 0; index < value; index += 1)
    {
      yield index;
    }
  }

  const isInError = ref(false);
  const errorMessage = ref("");
  const numberOfFields = ref(1);

  const headers = ref([]);
  const data = ref([]);

  const runApplication = (evt) =>
  {
    const params = [...evt.target.querySelectorAll('input')]
      .map(input => input.value);

    axios.post('http://localhost:8080/application.json', params)
      .then(response =>
      {
        if (response.data.type === 'success')
        {
          const responseData = response.data.data;

          isInError.value = false;
          errorMessage.value = "";

          if (responseData.length > 1)
          {
            headers.value = responseData[0];
            data.value = responseData.slice(1);
          }
          else if (responseData.length > 0)
          {
            headers.value = [];
            data.value = responseData;
          }
          else
          {
            headers.value = [];
            data.value = [];
          }
        }
        else
        {
          isInError.value = true;
          errorMessage.value = response.data.message;
        }
      })
      .catch(error => { isInError.value = true; });
  };

  const reset = () =>
  {
    isInError.value = false;
    errorMessage.value = "";

    headers.value = [];
    data.value = [];
  };

  const addField = () => { numberOfFields.value += 1; };
  const deleteField = () =>
  {
    numberOfFields.value -= 1;

    if (numberOfFields.value < 0)
    {
      numberOfFields.value = 0;
    }
  };
</script>

<style>
  @import "bootstrap/dist/css/bootstrap.min.css";
</style>
