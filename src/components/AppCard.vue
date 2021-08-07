<template>
    <div class="card">
       <div class="card-title">Столик № {{ couter }}</div>
       <div class="card-list" 
       v-for="(data , i) in list.reservation"
       :key="i">
        <div class="card-time">{{ data.time }}</div>
        <div class="card-text">Бронь</div>
        <div class="card-event" ><template v-if="data.event">new</template></div>
        <button class="card-view" @click="$emit('click' , {id: data.id , editor: true, index: i})">Смотреть</button>
        </div> 
        <button class="card-btn" @click="$emit('click' , {id: list.id , editor: false})">Забронировать</button>
    </div>




</template>

<script>
export default {
    emits: ['click'],
    props: {
        time: {
            type: String,
        },
        event: {
            type: Boolean,
        },
        list: {
            type: Array
        },
        couter: {
            type: Number
        },
    }
}
</script>

<style lang="sass" scoped>
.card
    background-color: var(--white)
    padding: 15px 20px
    border-radius: 15px
    box-shadow: 0px 0px 29px rgba(0, 0, 0, 0.45)
    max-width: 277px

    &-list
        display: grid
        grid-auto-flow: column
        justify-content: flex-start
        align-items: center
        grid-gap: 15px
        margin-bottom: 25px

    &-title
        display: grid
        grid-gap: 5px
        font-size: 24px
        font-weight: 400
        text-align: center
        margin-bottom: 15px

    &-time , &-text 
        font-weight: 600
        font-size: 18px

    &-time
        color: var(--red)

    &-text
        color: var(--black)

    &-event
        color: var(--red)
        font-size: 14px
        width: 39px
        font-weight: 600
        text-transform: uppercase


    &-view
        font-family: 'Montserrat', sans-serif
        font-weight: 500
        color: var(--black)
        font-size: 14px
        background: none
        border: none
        transition: 0.5s color
        will-change: color
        cursor: pointer

        &:hover
            color: var(--red)

    &-btn
        font-family: 'Montserrat', sans-serif
        letter-spacing: 1.5px
        display: block
        width: fit-content
        margin: 0 auto
        border: none
        padding: 13px 17px
        color: var(--white)
        font-weight: 600
        border-radius: 6px
        background: var(--red)
        text-transform: uppercase
        cursor: pointer
        transition: 0.5s box-shadow
        will-change: box-shadow

        &:hover
            box-shadow: 0 0 10px var(--red)


</style>