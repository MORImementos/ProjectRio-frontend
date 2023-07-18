import { STAT_ENDPOINTS, GET, CURRENT_SEASON_OFF } from '$lib/constants';
// import type { PageServerLoad } from './$types'

// fetch stats on page load
export const load = async () => {
    const data = await GET(STAT_ENDPOINTS.STATS + `?tag=${CURRENT_SEASON_OFF}`)
    // console.log(data);
    return {data: data}

}