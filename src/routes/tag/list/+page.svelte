<script lang="ts">
	import { GET, UNCATEGORIZED_ENDPOINTS } from "$lib/constants";
    import { onMount } from "svelte";

    onMount(async () => {
        const response = await GET(UNCATEGORIZED_ENDPOINTS.TAG_LIST)
        const res = await response.text()
        console.log(res)
    })
</script>