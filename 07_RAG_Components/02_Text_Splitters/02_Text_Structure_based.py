from langchain.text_splitter import RecursiveCharacterTextSplitter

text="""
On a misty morning in early spring, the valley wakes to the slow chorus of sparrows and the earthy scent of damp soil. Dew-flecked ferns uncurl beside the creek, while shafts of sunlight squeeze through the pines in thin golden ribbons. It is a scene that seems motionless at first, yet every second is full of tiny orchestras: the ripple of water over smooth stones, the near-silent hum of bees inspecting wild violets, and the breath of wind brushing one leaf against another.

Across the planet in a buzzing metropolis, algorithms run invisibly beneath the neon glow. Trains glide in on time because a predictive model shifted the schedule three milliseconds ago; storefronts adjust prices because a reinforcement-learning agent sensed lunchtime crowds. Though pedestrians stare at their phones, the city itself is thinking—optimizing traffic lights, balancing electrical grids, and mapping emergency routes that, luckily, most citizens will never need to know. Technology hums like a second heartbeat, steady and unseen.


Historians still debate whether the lost journal of Captain Reyes was genuine, but the fragments paint a vivid picture of an 18th-century voyage past Cape Horn. One entry describes forty-foot waves slamming the wooden hull “as if the very ocean had fists.” Another notes a sudden calm in which sailors caught sight of “twin rainbows bowed like celestial bridges.” If authentic, the pages remind us that exploration was equal parts terror and awe, recorded in salted ink.

“I’m telling you, Luna, the comet will be visible tonight,” Marco insisted, leaning over the telescope’s tripod.
She rolled her eyes. “You said that last week, and all I saw was a smudge of atmospheric distortion.”
“It wasn’t distortion—it was anticipation,” he replied, mouth curving into a grin. The two friends argued under the darkening sky until the first star appeared, silencing them both. In that hush, a slender silver streak finally grazed the horizon, proving at least one of them right.

"""

splitter=RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=10
)

chunks=splitter.split_text(text)

print(len(chunks))
print(chunks)

# we are gonna use this mostly
