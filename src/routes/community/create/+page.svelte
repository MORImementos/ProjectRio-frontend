<<<<<<< HEAD
<script lang="ts">
  // Instantiate variables
  let name: string = "";
  let type: string = "";
  let description: string = "";
  let priv: boolean = false;
  let createGlobalLink: boolean = false;

  async function handleSubmit() {
    if (!name || !type || !description || !priv || !createGlobalLink) {
      alert("Please completely fill out the form");
      return;
    }

    const formData = new FormData();
    formData.append("community_name", name);
    formData.append("type", type);
    formData.append("desc", description);
    formData.append("private", priv);
    formData.append("global_link", createGlobalLink);

    try {
      const response = await fetch("/community/create", {
        method: "POST",
        body: formData,
      });

      console.log(response);

      const jsonRes = await response.json();
      const result = jsonRes;

      console.log(result);
    } catch (error) {
      console.log(error);
    }
  }
</script>

<h1>Create Community</h1>
<form>
  <section class="input-container">
    <p>Community Name:</p>
    <input placeholder="Community Name" bind:value={name} />

    <p>Community Type:</p>
    <input placeholder="Community Type" bind:value={type} />

    <p>Description:</p>
    <input placeholder="Description" bind:value={description} type="password" />

    <p>Private:</p>
    <input bind:checked={priv} type="checkbox" />

    <p>Create Global Link:</p>
    <input bind:checked={createGlobalLink} type="checkbox" />

    <p></p>
    <button type="button" on:click={handleSubmit}>Submit</button>
  </section>
</form>

<style>
  h1 {
    text-align: center;
    margin: auto;
  }

  .input-container {
    margin: auto;
    max-width: 200px;
    display: grid;
  }
</style>
=======
<script lang="ts">
    import type { PageData } from './$types';
    import type { Writable } from 'svelte/store';
    import { superForm } from 'sveltekit-superforms/client';
    import SuperDebug from 'sveltekit-superforms/client/SuperDebug.svelte';
  
    export let data: PageData;
  
    // Client API:
    const { form, errors, constraints, enhance } = superForm(data.form);
    
  </script>
  
  {#if data}
  <!-- <div>{data.username}</div> -->
  {/if}
  <SuperDebug data={$form} />
  <div class="flex items-center justify-center h-screen ">
    <div class="p-4 md:p-10 flex bg-gradient-to-br variant-gradient-primary-secondary w-[80%] h-[80%] rounded-container-token shadow-2xl space-y-10">
  <form method="POST" class="flex card flex-col justify-center items-center mx-auto transition-[width] duration-200 w-[80%] h-full shadow-2xl" use:enhance>
    <div class="card flex flex-col p-4 m-2 text-token space-y-4 shadow-2xl w-[80%] h-[20%]">

    <label for="community_name">community name</label>
    <input
    class="text-primary-50-900-token"
    type="text"
    name="community_name"

    aria-invalid={$errors.community_name ? 'true' : undefined}
    bind:value={$form.community_name}
    {...$constraints.community_name} />
    {#if $errors.community_name}<span class="invalid">{$errors.community_name}</span>{/if}
</div>
<div class="card flex flex-col p-4 m-2 text-token space-y-4 shadow-2xl w-[80%] h-[20%]">

    <label for="type">type</label>
    <select
      class="text-primary-50-900-token"
      name="type"
      aria-invalid={$errors.type ? 'true' : undefined}
      bind:value={$form.type}
      {...$constraints.type}>
      <!-- <option value="">Select type</option> -->
      <option value="Unofficial" selected>Unofficial</option>
      <option value="Official">Official</option>
      <!-- <option value="option3">Option 3</option> -->
    </select>
    {#if $errors.type}<span class="invalid">{$errors.type}</span>{/if}
</div>
    <div class="card flex flex-col p-4 m-2 text-token space-y-4 shadow-2xl w-[80%] h-[15%]">
    <label for="private">private</label>
    <input
      type="checkbox"
      name="private"
      aria-invalid={$errors.private ? 'true' : undefined}
      bind:checked={$form.private}
      {...$constraints.private} />
    {#if $errors.private}<span class="invalid">{$errors.private}</span>{/if}
  </div>
  <div class="card flex flex-col p-4 m-2 text-token space-y-4 shadow-2xl w-[80%] h-[15%]">

    <label for="global_link">global link</label>
    <input
      type="checkbox"
      name="global_link"
      aria-invalid={$errors.global_link ? 'true' : undefined}
      bind:checked={$form.global_link}
      {...$constraints.global_link} />
    {#if $errors.global_link}<span class="invalid">{$errors.global_link}</span>{/if}
</div>
<div class="card flex flex-col p-4 m-2 text-token space-y-4 shadow-2xl w-[80%] h-[20%]">

    <label for="desc">description</label>
    <textarea
    class="text-primary-50-900-token"
        name="desc"
        aria-invalid={$errors.desc ? 'true' : undefined}
        bind:value={$form.desc}
        {...$constraints.desc}></textarea>
    {#if $errors.desc}<span class="invalid">{$errors.desc}</span>{/if}
</div>
<div class="card flex flex-col p-4 m-2 text-token space-y-4 shadow-2xl w-[80%] h-[10%]">
    
<button>Submit</button></div>
  </form>
  </div>
  </div>
  
  <style>
    .invalid {
      color: red;
    }
  </style>
  
>>>>>>> origin/update
