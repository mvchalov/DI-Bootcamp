class Video {
    constructor(title, uploader, time) {
        this.title = title;
        this.uploader = uploader;
        this.time = time;
    }

    watch() {
        return `${this.uploader} watched all ${this.time}s of "${this.title}"`
    }
}

const myVideo = new Video("Funny Cat Video", "Grumpy Racoon", 11);
console.log(myVideo.watch());

const myVideo2 = new Video("Star Wars under the sink", "Part Vader", 33);
console.log(myVideo2.watch());

const inData = [
    ["Funny Cat Video", "Grumpy Racoon", 11],
    ["Star Wars under the sink", "Part Vader", 33],
    ["Sad Cat Video", "Grumpy Racoon", 5],
    ["Lucky Cat Video", "Grumpy Racoon", 90],
    ["I'm your mother", "Part Vader", 11]
]

const funnyVideos = new Array(5).fill(undefined).map((e,i)=>new Video(...inData[i]));

funnyVideos.forEach(e=>{
    console.log(e.watch())
})