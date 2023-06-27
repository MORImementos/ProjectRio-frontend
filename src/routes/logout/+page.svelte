<script lang="ts">
    import { enhance } from "$app/forms";

</script>

<form 
    use:enhance
    action="/logout"    
    method="POST">
<button>
LOGOUT
</button>
</form>