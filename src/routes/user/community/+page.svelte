<script lang="ts">
    import { GET, USER_ENDPOINTS } from "$lib/constants";
    import { onMount } from "svelte";

    let data;
    onMount(async () => {
        const response = await GET(USER_ENDPOINTS.USER_COMMUNITY)
        const res = await response;
        console.log(res)
        data = res;
    })
</script>

{#if data}
    <div>{data}</div>
{/if}