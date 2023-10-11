import type { PageServerLoad, Actions } from "./$types";
import { communityInvite } from "$lib/zodSchema";
import { superValidate } from "sveltekit-superforms/server";
import {getAllUsers} from "$lib/helpers/allUsers";
import {fail} from "@sveltejs/kit";
import {BACKEND, COMMUNITY_ENDPOINTS} from "$lib/constants";

export const load: PageServerLoad = async ({ params, fetch }) => {
    const res = await getAllUsers();
    const users = await Object.values(res)
    // console.log(users)
    return {
        users: users,
        form: superValidate(communityInvite)
    };
};

export const actions = {
    default: async ({ request, fetch }) => {
        const form = await superValidate(request, communityInvite);

        // Convenient validation check:
        if (!form.valid) {
            // Again, always return { form } and things will just work. (superforms comment)
            return fail(400, { form });
        }

        // fetch request
        console.log(BACKEND + COMMUNITY_ENDPOINTS.COMMUNITY_CREATE)
        const response = await fetch(BACKEND + COMMUNITY_ENDPOINTS.COMMUNITY_INVITE, {
            headers: { 'Content-Type': 'application/json' },
            method: "POST",
            body: JSON.stringify(form.data),
        })

        console.log(response.status)
        // console.log('response', request.headers)
        // if community creation unsuccessful
        if (response.status !== 200) {
            return fail(response.status, { failed: true, form: form })
        }
        const res = await response.json();

        // if community creation successful
        if (response.status === 200) {
            // Handle the response as needed
            console.log(res)
            /* Yep, return { form } here too (apparently superforms really wants you to return forms)
            return form and any other relevant data
            TODO: Add any additional data you want to return */
            return {
                success: true,
                form: form,
            }
        }
    }
} satisfies Actions;