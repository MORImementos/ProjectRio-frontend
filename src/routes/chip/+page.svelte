<script>
    import { InputChip } from '@skeletonlabs/skeleton';

    let selectedItems = [];
    let availableItems = ['Item 1', 'Item 2', 'Item 3', 'Item 4'];

    function selectItem(item) {
        selectedItems = [...selectedItems, item];
        availableItems = availableItems.filter((i) => i !== item);
    }

    function removeItem(item) {
        selectedItems = selectedItems.filter((i) => i !== item);
        
        availableItems = [...availableItems, item];

    }
    // $: selectedItems = selectedItems
</script>

<div>
    <select class="select" multiple on:change={(e) => selectItem(e.target.textContent)}>
<!--        <option value="">Select an item...</option>-->
        {#each availableItems as item}
            <option value={item}>{item}</option>
        {/each}
    </select>

    <div class="chips">
        <!--{#each selectedItems as item}-->
            <InputChip
                    bind:value={selectedItems}
                    name="tags"
                    whitelist={availableItems}
                    on:click={(e) => removeItem(e.target.innerText)}
            />
            <!--    {item}-->
            <!--</InputChip>-->
        <!--{/each}-->
    </div>
</div>

<style>
    /* Add your custom styling here */
</style>
