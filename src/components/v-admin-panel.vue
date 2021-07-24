<template>
    <div class="v-admin-panel">
        <h1>ADMIN-PANEL</h1>
        <div>
            {{ reservation }}
        </div>
    </div>
</template>

<script>
export default {
    name: 'v-admin-panel',
    data: function() {
        return {
          connection: null,
          reservation: null
        }
    },

    methods: {
        socketMessage() {
            const message = JSON.parse(event.data);

            if (message.action === 'give_reservation') {
                this.reservation = message.data.reservation
            }
        },
        socketInit() {
            console.log("Starting connection to WebSocket Server")
            this.connection = new WebSocket(
                "ws://127.0.0.1:8000/connect"
                + "?token="
                + this.$store.state.user.token
            )

            this.connection.onmessage = this.socketMessage;

            this.connection.onopen = function(event) {
                console.log(event)
                console.log("Successfully connected to the echo websocket server...")
            }

            this.connection.onclose = function(event) {
                console.log(event);
                console.log("WebSocket is closed now.");
            }
        },
    },
    created() {
        this.$nextTick(() => {
            if (this.$store.state.user.token) {
                this.socketInit()
            }
        })
    },

}
</script>