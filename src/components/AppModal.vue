<template>
    <div class="modal">
        <div class="modal-overlay">
            <div class="modal-body">
                <button class="modal-close"  @click="$emit('close')"></button>
                <div class="modal-fields">
                    <input type="text" class="modal-field" placeholder="Имя" v-model="name">
                    <input type="text" class="modal-field"  placeholder="Фамилия" v-model="surname">
                    <input type="text" class="modal-field" placeholder="Номер телефона" v-model="phone">
                </div>
                <div class="modal-filter">
                  <select class="modal-select">
                    <option value="AVACADO">Avacado</option>
                    <option value="AVACADO">Avacado</option>
                    <option value="AVACADO">Avacado</option>
                  </select>
                  <select class="modal-select">
                    <option v-for="i in 10" :value="i" :key="i">{{i}}</option>
                  </select>
                  <select class="modal-select" v-model="start">
                    <option v-for="(item, idx) in availableTime" :key="idx" :value="item" :selected="item == start ? true : false"
                    >
                      {{ item }}
                    </option>
                  </select>
                  <select class="modal-select" v-model="end">
                    <option v-for="(item, idx) in availableTime" :key="idx" :value="item" :selected="item == end ? true : false"
                    >
                      {{ item }}
                    </option>
                  </select>
                </div>
                <textarea class="modal-field modal-area" placeholder="Пожелания" v-model="wishes"></textarea>
                <label class="modal-label">
                    <input type="checkbox" class="modal-checkbox" v-model="beforeArrival">
                    <div class="modal-decor">Забить кальян до прихода</div>
                </label>
                <div class="modal-btns">
                    <template v-if="editor">
                        <button class="modal-btn" @click="$emit('update')">Обновить заявку</button>
                    <button class="modal-btn"  @click="$emit('remove', {id: info.id, table: info.table, index: index})">
                    Отменить бронь</button>
                    </template>
                     <button v-else class="modal-btn"  @click="$emit('add')">Добавить бронь</button>
                </div>
            </div>
        </div>
    </div>
</template>


<script>
import axios from 'axios'
export default {
    emits: ['close', 'remove', 'update', 'add'],
    props: {
        show: {
            type: Boolean,
            default: false,
        },
        editor: {
            type: Boolean,
            required: true,
        },
        index: {
            type: Number
        },
        info: {
            type: Object,
            required: true,
        },
        availableTime: {
          type: Array,
          required: true,
        }
    },
    data: () => ({
        name: '',
        surname: '',
        phone: '',
        wishes: '',
        start: '',
        end: '',
        beforeArrival: false,
    }),

    created() {
        if (this.editor) {
            this.name = this.info.name
            this.surname = this.info.surname
            this.phone = this.info.phone_number
            this.wishes = this.info.wishes
            this.beforeArrival = this.info.before_arrival
            this.start = this.info.start
            this.end = this.info.end
        }
    }
}
</script>

<style lang="sass" scoped>
.modal

    &-overlay
        position: fixed
        inset: 0
        display: flex
        align-items: center
        justify-content: center
        background-color: rgba(0 , 0, 0, 0.5)

    &-body
        position: relative
        padding: 40px
        background-color: var(--black)
        border-radius: 34px

    &-close
        position: absolute
        right: 15px
        top: 15px
        width: 25px
        height: 25px
        color: rgba(255, 255, 255, 0.7)
        background: none
        border: none
        padding: 0
        transition: 0.5s color
        will-change: color
        cursor: pointer

        &:hover
            color: var(--green)

        &::before , &::after
            position: absolute
            content: ''
            left: 0
            top: calc(50% - 3px)
            width: 100%
            height: 3px
            background-color: currentColor
            pointer-events: none

        &::before
            transform: rotate(45deg)

        &::after
            transform: rotate(-45deg)
            

    &-field
        background: #454545
        border-radius: 32px
        padding: 18px 27px
        font-size: 24px
        color: rgba(255, 255, 255, 0.7)
        border: 1px solid  transparent
        outline: none
        transition: 0.5s border

        &:hover , &:focus
            border-color: var(--green)

    &-area
        display: block
        height: 75px
        resize: none
        font-size: 20px
        width: 85%

    &-fields
        display: grid
        grid-gap: 25px

    &-select
        background: none
        border: none
        font-size: 24px
        color: rgb(255 255 255 / 70%)
        border-bottom: 1px solid rgb(255 255 255 / 70%)
        outline: none

        option
            background: #000
            font-size: 18px
            cursor: pointer

    &-filter
        display: grid
        grid-template-columns: repeat(2 , max-content)
        grid-gap: 20px 24px
        margin: 30px 0

    &-label
        display: inline-block
        margin: 10px 0 25px 0

    &-checkbox
        display: none

        &:checked + .modal-decor::before
            background-color: var(--green)
            

    &-decor
        position: relative
        color:  rgb(255 255 255 / 70%)
        font-size: 16px
        padding-left: 25px
        cursor: pointer

        &::before
            position: absolute
            content: ''
            left: 0
            top: 0
            width: 15px
            height: 15px
            border: 1px solid #454545
            border-radius: 5px
            transition: 0.5s background-color

    &-btns
        display: grid
        grid-auto-flow: column
        grid-gap: 15px
        justify-content: center

    &-btn
        font-family: 'Montserrat', sans-serif
        border: none
        width: 100%
        background: var(--green)
        padding: 20px
        color: var(--white)
        font-weight: 500
        font-size: 16px
        border-radius: 20px
        cursor: pointer
        transition: 0.5s box-shadow

        &:hover
            box-shadow: 0 0 8px var(--green)

</style>