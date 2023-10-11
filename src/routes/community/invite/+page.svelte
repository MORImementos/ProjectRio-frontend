<script lang="ts">
    import { Form } from "formsnap"
    import type { PageData } from "./$types";
    import { communityInvite } from "$lib/zodSchema";
    import { Autocomplete, InputChip, ListBox, ListBoxItem } from '@skeletonlabs/skeleton';
    import type { AutocompleteOption } from '@skeletonlabs/skeleton';
    export let data: PageData;
    import {onMount} from "svelte";

    let selectedUsers: string[] = [];
    let users: string[] = [];
    let userInput = '';
    onMount(async () => {
        if (data) {
            users = data.users;
            console.log(users)
        }
    })


</script>

<Form.Root class="form" form={data.form} schema={communityInvite} let:config debug={true}>
    <Form.Field {config} name="community_name">
        <Form.Label>Community Name</Form.Label>
        <Form.Input class="input" type="text"/>
        <Form.Validation />
    </Form.Field>

    <Form.Field {config} name="invite_list">
        <Form.Label class="label">Invite List</Form.Label>
<!--        <select class="select" multiple="true" bind:group={data.form.invite_list}>-->
<!--            {#each users as user}-->
<!--                <option value={user}>{user}</option>-->
<!--            {/each}-->

<!--        </select>-->
        {#if users}
        <ListBox multiple class="flex-auto">
            <!--                                    Not Selected-->
            {#each users as user, index}
                {#if !(selectedUsers.includes(user))}

                    <ListBoxItem bind:group={selectedUsers} name="medium" value={user}>{user}</ListBoxItem>

                {/if}
            {/each}
        </ListBox>
        <ListBox multiple class="flex-auto">
            <!--                                    Selected-->
            {#each users as user, index}
                {#if selectedUsers.includes(user)}
                    <ListBoxItem bind:group={selectedUsers} name="medium" value={user}>{user}</ListBoxItem>
                {/if}
            {/each}
        </ListBox>
            {/if}
<!--        <div class="card">{Object.values(selectedUsers)}</div>-->


        <Form.Validation />
    </Form.Field>

    <button class="btn variant-filled-primary" type="submit">Submit</button>
</Form.Root>


