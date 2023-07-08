import { z } from 'zod'
import { USERNAME_CHARACTER_LIMIT, PASSWORD_CHARACTER_LIMIT, EMAIL_CHARACTER_LIMIT, COMMUNITY_CHARACTER_LIMIT } from './constants';

/* Zod schemas / module are used because
    a) it is needed to work with superforms
    b) it allows for clean validation for form data / types
    c) you can pick and choose from schema to choose what to include in forms (for example, on login page, I only used Email and Password fields from the User object)
*/

// user validation
export const User = z.object({
    Email: z
        .string({ required_error: 'Email is required' })
        .email({ message: 'Please enter a valid email address' })
        .max(EMAIL_CHARACTER_LIMIT, { message: 'Email is too long' })
        .trim(),
    Password: z
        .string({ required_error: 'Password is required' })
        .min(1, { message: 'Please enter a valid password' })
        .max(PASSWORD_CHARACTER_LIMIT, { message: 'Password is too long' })
        .trim(),
    Username: z
        .string({ required_error: 'Username is required' })
        .min(1, { message: 'Please enter a valid username' })
        .max(USERNAME_CHARACTER_LIMIT, { message: 'Password is too long' })
        .trim()
})

type User = z.infer<typeof User>

// community validation
// TODO: finish this, possibly figure out a more efficient way to set up schema
export const Community = z.object({
    community_name: z
        .string({ required_error: 'Enter a valid community name' })
        .max(COMMUNITY_CHARACTER_LIMIT, { message: 'Community name is too long' })
        .min(1, { message: 'Community name is too short' })
        .trim(),
    type: z
        .enum(["Official", "Unofficial"], { required_error: 'Enter a valid type' }),
    private: z
        .union([
            z.literal('on').transform(() => true),
            z.literal('undefined').transform(() => false),
        ])
        .default(false)
        .optional(),
    global_link: z
        .union([
            z.literal('on').transform(() => true),
            z.literal('undefined').transform(() => false),
        ])
        .default(false)
        .optional(),
    desc: z
        .string({ required_error: 'Enter a valid description' })
        .max(1000, { message: 'Community description is too long' })
        .min(1, { message: 'Community description is too short'})
        .trim(),
})

// name as gamemodes insted?

export const Tagset = z.object({
    name: z
        .string({ required_error: 'Enter a valid name' })
        .max(100, { message: 'Name is too long'})
        .min(1, { message: 'Name is too short'})
        .trim(),
    desc: z
        .string({ required_error: 'Enter a valid description' })
        .max(1000, { message: 'Community description is too long' })
        .min(1, { message: 'Community description is too short'})
        .trim(),
    type: z
        .enum(["Tournament", "Season", "Ladder"], { required_error: 'Enter a valid type' }),
    community_name: z
        .string({ required_error: 'Enter a valid community name' })
        .max(COMMUNITY_CHARACTER_LIMIT, { message: 'Community name is too long' })
        .min(1, { message: 'Community name is too short' })
        .trim(),
    tags: z
        .array(z.number()),
    tag_set_id: z
        .number(),
    start_date: z
        .number()
        .transform((val) => new Date(val), (val) => val.getTime().toString()),
    end_date: z
        .number()
        .transform((val) => new Date(val), (val) => val.getTime().toString()),

})

export const GenericForm = z.object({
    GenericArray: z
        .array(z.string()).min(1)
})

