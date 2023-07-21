import { z } from 'zod';
import { superValidate } from 'sveltekit-superforms/server';
import { Tagset } from '$lib/zodSchema';
import { fail, redirect } from '@sveltejs/kit';
import { BACKEND, UNCATEGORIZED_ENDPOINTS } from '$lib/constants';
import type { Actions } from './$types';

// assign schema for form
const tagsetCreate = Tagset.pick({
    name: true,
    desc: true,
    type: true,
    community_name: true,
    tags: true,
    tag_set_id: true,
    start_date: true,
    end_date: true,
})

// infer type of schema
type tagsetCreate = z.infer<typeof tagsetCreate>

// on page load, check for jwt and redirect if jwt present
export const load = async ({ event, cookies }) => {
    const jwt = cookies.get('jwt')
    if (!jwt) throw redirect(302, '/login');

    const form = await superValidate(event, tagsetCreate);
    return {
        form
    };
};

// on submit if form is valid, create community. if not, throw error
export const actions = {
    default: async ({ request, fetch }) => {
        const form = await superValidate(request, tagsetCreate);

        if (!form.data.tag_set_id > 0) {
            delete form.data.tag_set_id
            console.log(form.data)
        }
        // Convenient validation check:
        if (!form.valid) {
            // Again, always return { form } and things will just work. (superforms comment)
            return fail(400, { form });
        }
        
        console.log(form.data)
        // fetch request
        console.log(BACKEND + UNCATEGORIZED_ENDPOINTS.CREATE_TAG_SET)
        const response = await fetch(BACKEND + UNCATEGORIZED_ENDPOINTS.CREATE_TAG_SET, {
            headers: { 'Content-Type': 'application/json' },
            method: "POST",
            body: JSON.stringify(form.data),
        })
        
        console.log(response.status)
        // if community creation unsuccessful
        if (response.status !== 200) {
        {
            // This is all just a way to parse the HTML error received. I'm still not certain if I intend to do anything with it or not yet since a generic error might be all that's needed.
            const reader = response.body?.getReader();
            const reading = true;
            const errorObj = {};

            while (reading) {
                const { done, value } = (reader ?? {}).read(); // Use nullish coalescing operator to handle undefined reader
            if (done) break;
            const val = new TextDecoder().decode(value);
            errorObj[val] = val;
        }

  // Return error
  return fail(response.status, { form });
            }
        }
        const res = await response.json();

        // if community creation successful
        if (response.status === 200) {
            // Handle the response as needed
            console.log(res)
        }

        /* Yep, return { form } here too (apparently superforms really wants you to return forms)
        return form and any other relevant data
        TODO: Add any additional data you want to return */
        return {
            form: form,
            msg: res.msg,
            username: res.username
        }
    }
} satisfies Actions;
