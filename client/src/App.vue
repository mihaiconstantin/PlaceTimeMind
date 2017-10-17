<template>
  <div id="app" class="container shadow-container">
    <h1 class="display-4 text-center">A place and time for things<br>and mind</h1>
    <hr>

    <div class="row">
      <form class="col-md-7 mr-auto ml-auto">
        <div class="form-group">
          <label for="commit">My commitment:</label>
          <textarea id="commit" class="form-control" rows="4" v-model="newCommit" 
                    placeholder="Start with I will... and mention a place and time..."
          ></textarea>
        </div>
        <button type="submit" class="btn btn-secondary" @click="addCommit">Commit</button>
      </form>
    </div>

    <hr>

    <div class="row commits">
      
      <div class="col-md-7 mr-auto ml-auto">
        <h1 class="display-1">I will...</h1>
      </div>
    
      <div class="col-md-6 mr-auto ml-auto">
        <ul class="list-unstyled">
          <li 
            class="noselect shadow" 
            v-for="commit in allCommits" 
            v-bind:class="{ done: commit.done }" 
            @dblclick="disableCommit(commit, $event)"
            >{{ commit.msg }}<small> - {{ commit.date }}</small></li>
        </ul>
      </div>
    </div>
    
    <hr>

    <footer class="row text-center">
      <small class="col-md-12">Have a great day! &#9728;</small>
    </footer>

  </div>
</template>

<script>
  export default {
    data () {
      return {
        oldCommits:[],
        newCommits:[],
        newCommit: '',
         monthNames: ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
      }
    },

    computed: {
      allCommits() {
        return this.newCommits.concat(this.oldCommits);
      }
    },

    created: function () {
      this.loadCommits();
    },

    methods: {
      addCommit(event) {
        event.preventDefault();
        if (this.newCommit == "") return;

        var date = new Date();
        var when = `${this.monthNames[date.getMonth()]} ${date.getDay()}, ${date.getFullYear()}`;
        var commitObj = {
          msg: this.newCommit.replace('I will ', ''),
          date: when,
          done: false
        }
        this.newCommit = '';
        this.newCommits.unshift(commitObj);
        this.saveChanges();
      },

      disableCommit(commit) {
        commit.done = !commit.done;
        this.saveChanges();
      },

      loadCommits() {
        var that = this;
        jQuery.ajax({
          url: '/commits',
          type: 'GET',
          contentType: 'application/json',
          success: function(response) {
            that.oldCommits = JSON.parse(response);
          }
        });
      },

      saveChanges() {
        jQuery.ajax({
          url: '/commits',
          type: 'POST',
          data: {commits: JSON.stringify(this.allCommits)},
          dataType: 'json',
          success: function(response) {
            if (response == 'ok') {
              console.log('Changes saved. Thank you.');
            } else {
              console.log('Something went wrong.');
            }
          }
        }); 
      }

    }
  }
</script>

<style lang="scss">
  body {
    background-color: royalblue;
    color: #fff;
  }

  hr {
    background-color: #FFF;
    width: 2rem;
    margin: 3rem auto;
  }

  .container {
    margin-top: 3rem;
    margin-bottom: 3rem;
    padding-top: 1rem;
    padding-bottom: 1rem;
    border: 1px solid rgba(255, 255, 255, .05);
    border-radius: 3rem;
  }

  .commits {
    margin-bottom: 3rem;

    h1 {
      margin-bottom: 1rem;
    }
  }

  li {
    font-style: italic;
    line-height: 2rem;
    cursor: pointer;
    padding: 1rem 2.5rem 1rem 2.5rem;
    background-color: rgba(255, 255, 255, .1);
    border-radius: 5rem;
    margin-bottom: 1rem;

    small {
      font-size: .6rem;
      font-style: normal;
      display: block;
      text-align: right;
      line-height: 1rem;
    }
  }

  li:hover{
    /*background-color: rgba(255, 255, 255, .15);*/
  }

  .done {
    text-decoration: line-through;
    color: #CCC;
    opacity: 0.5;
  }

  .noselect {
    -webkit-touch-callout: none; /* iOS Safari */
      -webkit-user-select: none; /* Safari */
       -khtml-user-select: none; /* Konqueror HTML */
         -moz-user-select: none; /* Firefox */
          -ms-user-select: none; /* Internet Explorer/Edge */
              user-select: none; /* Non-prefixed version, currently
                                    supported by Chrome and Opera */
  }

  .shadow-container {
    box-shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22);
  }

  .shadow {
    box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
    transition: all 0.3s cubic-bezier(.25,.8,.25,1);
  }
  .shadow:hover {
    box-shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22);
  }

  footer {
    color: #ffff00;
  }
</style>
