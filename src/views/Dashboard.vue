<template>
  <div class="wrapper">
    <div class="dashboard-header">
      <router-link to="/?exit" class="dashboard-exit">
        <img src="@/assets/svg/exit.svg" />
        Выйти из системы
      </router-link>
      <h1 class="dashboard-title">Приветствую {{ name }}</h1>
    </div>
    <div class="dashboard-list">
      <app-card
      v-for="(card , i) in cards"
      :key="card.id"
      :couter="i + 1"
      :list="card"
      @click="openModal($event)"
      ></app-card>
    </div>
  </div>


    <app-modal
    @close="showModal = !showModal"
    :editor="editor"
    :info="info"
    :index="index"
    :availableTime="availableTime"
    @remove="remove($event)"
    v-if="showModal"
    ></app-modal>
</template>



<script>
import AppCard from "@/components/AppCard";
import AppModal from "@/components/AppModal";
export default {
  components: {
    AppCard,
    AppModal
  },
  data: () => ({
    name: "Андрей",
    index: null,
    showModal: false,
    editor: false,
    cards: null,
    availableTime: [
      '13:00', '13:30',
      '14:00', '14:30',
      '15:00', '15:30',
      '16:00', '16:30',
      '17:00', '17:30',
      '18:00', '18:30',
      '19:00', '19:30',
      '20:00', '20:30',
      '21:00', '21:30',
      '22:00', '22:30',
      '23:00', '23:30',
      '00:00', '00:30',
      '01:00',
    ]
  }),

    methods: {
        openModal({id, editor, index}){
            if (editor) {
              axios.get(`api/reservation/reservation-detail/${id}`)
              .then(({data}) => {
                this.info = data
                this.showModal = true
              })
            } else {
              this.showModal = true
            }
            this.index = index
            this.editor = editor
        },
        remove(event) {
            console.log(event)
            axios.delete(`api/reservation/reservation-delete/${event.id}`)
            .then((data) => {
                this.showModal = false
                // TODO: delete reservation in cards
            })
        },
        socketMessage() {
            const message = JSON.parse(event.data);
            if (message.action === 'give_reservation') {
                this.cards = message.data.reservation
            }
            if (message.action === 'add_reservation') {
                const index = this.cards.findIndex(function(voteItem) {
                    return voteItem.id == message.data.detail.id 
                })
                this.cards[index].reservation.push(message.data.detail.reservation[0])
            }
        },
        socketInit() {
            console.log("Starting connection to WebSocket Server")
            this.connection = new WebSocket(
                "ws://127.0.0.1:8000/connect"
                + "?token="
                + localStorage.getItem('token')
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
        if (localStorage.getItem('token')) {
            this.socketInit()
        }
      })
    },
};
</script>


<style lang="sass" scoped>
.dashboard
    &-header
        display: flex
        justify-content: space-between
        align-items: center
        padding-top: 50px
        margin-bottom: 38px

    &-title
        margin: 0 auto
        font-weight: 500
        font-size: 36px
        color: var(--black)

    &-list
        display: grid
        grid-template-columns: repeat(auto-fill ,  332px )
        justify-content: center
        align-items: center
        grid-gap: 57px

    &-exit
        text-decoration: none
        color: var(--black)
        font-size: 24px

</style>

