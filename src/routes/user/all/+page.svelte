<script lang="ts">
    import {onMount} from "svelte";

    export let data;
    import { Table } from '@skeletonlabs/skeleton'
    import type {PaginationSettings} from "@skeletonlabs/skeleton";
    import { Paginator } from "@skeletonlabs/skeleton";

    let users;
    let paginationSettings;

    onMount(async () =>{
        users = await data.users;
        console.log(users)
    })

    let header = ['Username']




</script>
{#if users}
<!--    <Table source={{ head: header, body: users }} />-->
    <div class="table-container overflow-y-scroll">
        <table class="table table-compact">
            <thead>
                <tr>
                    <th>Username</th>
                </tr>
            </thead>
            <tbody>

            {#each Object.values(users) as user}
                <tr>
                    <td>{user}</td>
                </tr>
            {/each}
            </tbody>
        </table>
    </div>
{:else}
    <div class="placeholder" />
{/if}