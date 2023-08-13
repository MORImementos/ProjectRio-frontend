<script>
    import {getAllUsers} from "$lib/helpers/allUsers";
    let data;

    data = getAllUsers()

</script>

{#if data}
    {#each data as user}
        <div>{user}</div>
    {/each}
{/if}