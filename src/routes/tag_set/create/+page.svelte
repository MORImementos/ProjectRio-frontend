<script lang="ts">
    import type { PageData } from './$types';
    import { superForm } from 'sveltekit-superforms/client';
    import SuperDebug from 'sveltekit-superforms/client/SuperDebug.svelte';
  
    export let data: PageData;
  
    // Client API:
    const { form, errors, constraints, enhance } = superForm(data.form);
  
  </script>
    <SuperDebug data={$form} />

  {#if data}
  <!-- <div>{data.username}</div> -->
  {/if}
  <!-- <SuperDebug data={$form} /> -->
  <div class="flex items-center justify-center h-screen ">
    <div class="p-4 md:p-10 flex bg-gradient-to-br variant-gradient-primary-secondary w-[80%] h-full rounded-container-token shadow-2xl space-y-10">
  <form method="POST" class="flex card flex-col justify-center items-center mx-auto transition-[width] duration-200 w-[80%] h-full shadow-2xl" use:enhance>

    <div class="card flex flex-col p-4 m-2 text-token space-y-4 shadow-2xl w-[80%] h-[20%]">

      <label for="name">name</label>
      <input
      class="text-primary-50-900-token"
      type="text"
      name="name"
  
      aria-invalid={$errors.name ? 'true' : undefined}
      bind:value={$form.name}
      {...$constraints.name} />
      {#if $errors.name}<span class="invalid">{$errors.name}</span>{/if}
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
  <div class="card flex flex-col p-4 m-2 text-token space-y-4 shadow-2xl w-[80%] h-[20%]">

    <label for="type">type</label>
    <select
      class="text-primary-50-900-token"
      name="type"
      aria-invalid={$errors.type ? 'true' : undefined}
      bind:value={$form.type}
      {...$constraints.type}>
      <!-- <option value="">Select type</option> -->
      <option value="Season" selected>Season</option>
      <option value="League">League</option>
      <option value="Tournament">Tournament</option>

      <!-- <option value="option3">Option 3</option> -->
    </select>
    {#if $errors.type}<span class="invalid">{$errors.type}</span>{/if}
</div>
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

    <div class="card flex flex-col p-4 m-2 text-token space-y-4 shadow-2xl w-[80%] h-[15%]">
    <label for="tags">tags</label>
    <input
      type="checkbox"
      name="tags"
      aria-invalid={$errors.tags ? 'true' : undefined}
      bind:checked={$form.tags}
      {...$constraints.tags} />
    {#if $errors.tags}<span class="invalid">{$errors.tags}</span>{/if}
  </div>
  <div class="card flex flex-col p-4 m-2 text-token space-y-4 shadow-2xl w-[80%] h-[15%]">

    <label for="tag_set_id">tagset id</label>
    <input
      type="checkbox"
      name="tag_set_id"
      aria-invalid={$errors.tag_set_id ? 'true' : undefined}
      bind:checked={$form.tag_set_id}
      {...$constraints.tag_set_id} />
    {#if $errors.tag_set_id}<span class="invalid">{$errors.tag_set_id}</span>{/if}
</div>
<div class="card flex flex-col p-4 m-2 text-token space-y-4 shadow-2xl w-[80%] h-[15%]">

  <label for="start_date">start date</label>
  <input
    type="date"
    name="start_date"
    aria-invalid={$errors.start_date ? 'true' : undefined}
    bind:value={$form.start_date}
    {...$constraints.start_date} />
  {#if $errors.start_date}<span class="invalid">{$errors.start_date}</span>{/if}
</div>
<div class="card flex flex-col p-4 m-2 text-token space-y-4 shadow-2xl w-[80%] h-[15%]">

  <label for="end_date">end date</label>
  <input
    type="date"
    name="end_date"
    aria-invalid={$errors.end_date ? 'true' : undefined}
    bind:value={$form.end_date}
    {...$constraints.end_date} />
  {#if $errors.end_date}<span class="invalid">{$errors.end_date}</span>{/if}
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
  