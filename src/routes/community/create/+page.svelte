<script lang="ts">
    import type { PageData } from './$types';
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
  
  <form method="POST" use:enhance>
    <label for="community_name">community name</label>
    <input
    type="text"
    name="community_name"
    aria-invalid={$errors.community_name ? 'true' : undefined}
    bind:value={$form.community_name}
    {...$constraints.community_name} />
    {#if $errors.community_name}<span class="invalid">{$errors.community_name}</span>{/if}

    <label for="type">type</label>
    <select
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
  
    <label for="private">private</label>
    <input
      type="checkbox"
      name="private"
      aria-invalid={$errors.private ? 'true' : undefined}
      bind:checked={$form.private}
      {...$constraints.private} />
    {#if $errors.private}<span class="invalid">{$errors.private}</span>{/if}
  
    <label for="global_link">global link</label>
    <input
      type="checkbox"
      name="global_link"
      aria-invalid={$errors.global_link ? 'true' : undefined}
      bind:checked={$form.global_link}
      {...$constraints.global_link} />
    {#if $errors.global_link}<span class="invalid">{$errors.global_link}</span>{/if}

    <label for="desc">description</label>
    <textarea
        name="desc"
        aria-invalid={$errors.desc ? 'true' : undefined}
        bind:value={$form.desc}
        {...$constraints.desc}></textarea>
    {#if $errors.desc}<span class="invalid">{$errors.desc}</span>{/if}

    <div><button>Submit</button></div>
  </form>
  
  <style>
    .invalid {
      color: red;
    }
  </style>
  