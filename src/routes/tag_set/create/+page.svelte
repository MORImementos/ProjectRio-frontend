<script lang="ts">
    import type {PageData} from './$types';
    import {superForm} from 'sveltekit-superforms/client';
    import SuperDebug from 'sveltekit-superforms/client/SuperDebug.svelte';
    import {UNCATEGORIZED_ENDPOINTS, GET} from "$lib/constants";
    import {AlertTriangle} from 'lucide-svelte';
    import {InputChip} from '@skeletonlabs/skeleton'

    export let data: PageData;
    export let form;
    import {onMount} from 'svelte';
    import type {ConicStop} from '@skeletonlabs/skeleton';
    import {getAllTagSets} from "$lib/helpers/tagNames";
    import {tagsets} from "$lib/stores/tagsets";
    // Client API:
    const {form: formData, errors, constraints, enhance, delayed} = superForm(data.form);
    const conicStops: ConicStop[] = [
        {color: 'transparent', start: 0, end: 25},
        {color: 'rgb(var(--color-primary-900))', start: 75, end: 100}
    ];
    let tags = [];
    let tagset = [];
    let tagNames = [];
    let tagIds = [];

    onMount(async () => {
        try {
            const [response, tagSetsResponse] = await Promise.all([
                GET(UNCATEGORIZED_ENDPOINTS.TAG_LIST),
                getAllTagSets()
            ]);

            const res = await response;
            const tagSets = await tagSetsResponse;

            tags = res.Tags;
            tags.forEach(i => {
                tagNames.push(i.name)
                tagIds.push(i.id)
            })
            console.log(tagNames, tagIds)
            console.log(tags);

            // Use tagSets data here
            tagset = $tagsets
            // console.log(tagSets);
        } catch (error) {
            // Handle any errors
            console.error(error);
        }
    });


    let showSelect = false;

    function toggleSelect() {
        showSelect = !showSelect;
        if (!showSelect) {
            $formData.tag_set_id = undefined; // Clear the selection when hiding the select element
        }
    }

    // export function unixTimeFromDate(date) {
    //     return Math.floor(new Date (date).getTime() / 1000);
    // }
</script>
<SuperDebug data={$formData}/>
{#if form}
    <p>{form.name} created.</p>
{:else}
    {#if tags}
        <form method="POST" class="card flex-col" use:enhance>
            {#if $errors._errors}
                <aside class="alert variant-filled-error mt-6">
                    <div>
                        <AlertTriangle size="42"/>
                    </div>
                    <div class="alert-message">
                        <h3 class="h3">{"Form Submission Problem"}</h3>
                        <p>{$errors._errors}</p>
                    </div>
                </aside>
            {/if}

            <div class="m-6">

                <label class="label" for="name">Name</label>
                <input
                        class="input text-token"
                        type="text"
                        name="name"

                        aria-invalid={$errors.name ? 'true' : undefined}
                        bind:value={$formData.name}
                        {...$constraints.name}/>
                {#if $errors.name}<small class="invalid">{$errors.name}</small>{/if}
            </div>
            <div class="m-6">

                <label class="label" for="desc">Description</label>
                <textarea
                        class="textarea text-token"
                        row="4"
                        name="desc"
                        placeholder="Enter description of this game mode."
                        aria-invalid={$errors.desc ? 'true' : undefined}
                        bind:value={$formData.desc}
                        {...$constraints.desc}></textarea>
                {#if $errors.desc}<span class="invalid">{$errors.desc}</span>{/if}
            </div>
            <div class="m-6">

                <label class="label" for="type">Type</label>
                <select
                        class="select text-token"
                        name="type"
                        aria-invalid={$errors.type ? 'true' : undefined}
                        bind:value={$formData.type}
                        {...$constraints.type}>
                    <option value="Season" selected>Season</option>
                    <option value="League">League</option>
                    <option value="Tournament">Tournament</option>

                </select>
                {#if $errors.type}<span class="invalid">{$errors.type}</span>{/if}
            </div>
            <div class="m-6">

                <label class="label" for="community_name">community name</label>
                <input class="input text-token"
                       type="text"
                       name="community_name"

                       aria-invalid={$errors.community_name ? 'true' : undefined}
                       bind:value={$formData.community_name}
                       {...$constraints.community_name}/>
                {#if $errors.community_name}<span class="invalid">{$errors.community_name}</span>{/if}
            </div>

            <div class="m-6">
                <div class="tags">
                    <label class="label" for="tags">Tags</label>
                    <!--          <select class="select" multiple name="tags" bind:value={$formData.tags} >-->
                    <select class="select" multiple name="tags" bind:value={$formData.tags}>

                        {#each tags as tag, index}
                            <!--          <span class="chip variant-soft hover:variant-filled">-->
                            <!--            <span>(icon)</span>-->
                            <!--            <span>Action</span>-->
                            <!--          </span>-->
                            <option value={tag.id}>{tag.name}</option>
                        {/each}

                    </select>
                    <!--        <select class="select" multiple>-->
                    <!--          {#each tags as tag}-->
                    <!--          <span class="chip variant-soft hover:variant-filled">-->
                    <!--            <span>(icon)</span>-->
                    <!--            <span>Action</span>-->
                    <!--          </span>-->
                    <!--            <option value={tag.name}>{tag.name}</option>-->
                    <!--          {/each}-->

                    <!--        </select>-->
                    {#if $errors.tags}<span class="invalid">{$errors.tags}</span>{/if}
                </div>
                <!--      <div class="chips">-->
                <!--        <InputChip name="tags" bind:value={tags} placeholder="Tags..." />-->

                <!--      </div>-->
            </div>
                <div class="m-6">
                  <div class="tag_set_id">
                      <label>
                          <input type="checkbox" on:change={toggleSelect} />
                          Show Tagsets
                      </label>
                    <label class="label" for="tag_set_id">tagset id</label>
                      {#if showSelect}

                      <select class="select" name="tag_set_id" bind:value={$formData.tag_set_id}>
                          <option value={0}>Select a tagset</option>

                          {#each tagset as t}
                      <span class="chip variant-soft hover:variant-filled">
                        <span>(icon)</span>
                        <span>Action</span>
                      </span>
                        <option value={t.id}>{t.name}</option>
                      {/each}

                    </select>
                          {/if}
                    {#if $errors.tag_set_id}<span class="invalid">{$errors.tag_set_id}</span>{/if}
                  </div>
                  <div class="chips">

                  </div>
                </div>
            <div class="m-6">
                <label class="label" for="start_date">start date</label>
                <input class="input variant-form-material"
                       type="date"
                       name="start_date"
                       aria-invalid={$errors.start_date ? 'true' : undefined}
                       bind:value={$formData.start_date}
                       {...$constraints.start_date}/>
                {#if $errors.start_date}<span class="invalid">{$errors.start_date}</span>{/if}
            </div>
            <div class="m-6">

                <label class="label" for="end_date">end date</label>
                <input class="input variant-form-material"
                       type="date"
                       name="end_date"
                       aria-invalid={$errors.end_date ? 'true' : undefined}
                       bind:value={$formData.end_date}
                       {...$constraints.end_date}/>
                <!--           on:change={() => $formData.end_date = unixTimeFromDate(new Date($formData.end_date))}-->


                {#if $errors.end_date}<span class="invalid">{$errors.end_date}</span>{/if}
            </div>
            <div class="m-6">
                <button class="btn">Submit</button>
            </div>

            <!--    <button type="submit" class="btn variant-filled-primary w-full"-->
            <!--    >{#if $delayed}<ConicGradient stops={conicStops} spin width="w-6" />{:else}{"submit"}{/if}</button-->
            <!--    >-->
        </form>
    {/if}

{/if}