from typing import List

from Particle import Particle
from Vector import Vector

Particles = List[Particle]
Forces = List[Vector]

G = 1


def kinetic_energy(particles: Particles):
    '''
    Method to calculate the total kinetic energy of a system
     given a list of particles.
    :param particles: list of Particle objects
    :return float: total kinetic energy
    '''
    ke_total = 0
    for particle in particles:
        ke_total += particle.kinetic_energy()

    return ke_total


def potential_energy(particles: Particles):
    '''
    Method that calculates the total potential energy of the system.
    :param particles:
    :return:
    '''
    pe_total = 0
    for this_particle in particles:
        for other_particle in particles:
            if this_particle.label is not other_particle.label:
                sep = this_particle.position - other_particle.position
                pe_total += (-G * this_particle.mass * other_particle.mass) / abs(sep)

    return pe_total


#TODO fix this, need to find the counter wise components summed in the opposite direction.
def grav_force(particles: Particles):
    forces = []
    for this_particle in particles:
        this_force = Vector()
        for other_particle in particles:
            if this_particle.label is not other_particle.label:
                sep = this_particle.position - other_particle.position
                f = sep.unit_hat() * this_particle.mass * other_particle.mass * -1
                this_force += f.scalar_divide(abs(sep)**2)
        forces.append(this_force)
    return forces









